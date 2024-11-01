import socket
import threading
import random
import string
from threading import Lock
from google.protobuf.message import DecodeError
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
from abc import abstractmethod

from e2t.oms import BYMA_Messages_pb2 as pb


class E2T_OMS_BYMA:

    def __init__(self):
        self.connected = False
        self.reconnecting = False
        self.lock = Lock()

    @abstractmethod
    def status(self, clOrdID, orderID, quantity, price, live, cumQty, leavesQty, avgPx, lastPx):
        pass

    @abstractmethod
    def reject(self, idRef, reason):
        pass

    @abstractmethod
    def trade(self, orderId, execId, time, lastQty, lastPx, avgPx, cumQty):
        pass

    def connect(self, HOST, PORT):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((HOST, PORT))

            print(f"Connected to {HOST}:{PORT}...")
            self.connected = True

            self.client_thread = threading.Thread(target=self.handle_client, args=(HOST, PORT), daemon=True)
            self.client_thread.start()
            self.send_token_req("666", 'clientID')

        except socket.error as e:
            print(f"Error connecting to {HOST}:{PORT}: {e}")
            return

    def handle_client(self, HOST, PORT):
            buffer = b""
            while True:
                try:
                    data = self.client.recv(1024)

                    if not data:
                        print("Connection closed by server")
                        self.connected = False
                        break

                    buffer += data

                    while len(buffer) >= 5:
                        try:
                            size, new_pos = _DecodeVarint32(buffer, 0)
                        except IndexError:
                            break

                        if len(buffer) < new_pos + size:
                            break

                        message = pb.Message()
                        message.ParseFromString(buffer[new_pos:new_pos + size])

                        self.process_message(message)
                        buffer = buffer[new_pos + size:]

                except (socket.timeout, socket.error, DecodeError, Exception) as e:
                    print(f"Connection error: {e}, attempting to reconnect...")
                    buffer = b""  # Limpia el buffer
                    self.reconnect(HOST, PORT)
                    break

    def reconnect(self, HOST, PORT):
        with self.lock:
            if self.reconnecting:
                print("Already attempting to reconnect, skipping...")
                return

            self.reconnecting = True
            self.close_socket()

            try:
                self.connect(HOST, PORT)
            except Exception as e:
                print(f"Error during reconnection: {e}")
            finally:
                self.reconnecting = False

    def close_socket(self):
        if self.client:
            try:
                self.client.shutdown(socket.SHUT_RDWR)
                self.client.close()
            except socket.error as e:
                print(f"Error while closing socket: {e}")
            finally:
                self.client = None
                self.connected = False

    def process_message(self, message):
            if message.messageType == pb.MessageType.ORDER_STATUS:
                self.status(
                    message.orderStatus.clOrdID,
                    message.orderStatus.orderID,
                    message.orderStatus.quantity,
                    message.orderStatus.price,
                    message.orderStatus.live,
                    message.orderStatus.cumQty,
                    message.orderStatus.leavesQty,
                    message.orderStatus.avgPx,
                    message.orderStatus.lastPx
                )
            elif message.messageType == pb.MessageType.TRADE_ORDER:
                self.trade(
                    message.tradeOrder.orderID,
                    message.tradeOrder.execID,
                    message.tradeOrder.time,
                    message.tradeOrder.lastQty,
                    message.tradeOrder.lastPx,
                    message.tradeOrder.avgPx,
                    message.tradeOrder.cumQty
                )
            elif message.messageType == pb.MessageType.REJECT:
                self.reject(
                    message.reject.idRef,
                    message.reject.reason
                )
            elif message.messageType == pb.MessageType.TOKEN_RESPONSE:
                self.token = message.tokenResponse.token
            else:
                print(f"Unknown message type: {message.messageType}")

    def send_order(self, order_buffer):
        try:
            if self.client:
                size = len(order_buffer)
                self.client.sendall(_VarintBytes(size) + order_buffer)
            else:
                print("Error: Client not available")
        except socket.error as e:
            print(f"Error sending order: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def send_token_req(self, clientID, busID):
        try:
            token_request = pb.TokenRequest(
                clientID=str(clientID),
                busID=busID
            )
            message = pb.Message(
                messageType=pb.MessageType.TOKEN_REQUEST,
                tokenRequest=token_request
            )
            buffer = message.SerializeToString()
            self.send_order(buffer)
        except Exception as e:
            print(f"Error creating token request: {e}")

    def send_limit_order(self, clOrdID, side, securityID, quantity, price, timeInForce, expireTime, settlType, account, display):
        try:
            extended_clOrdID = self.generate_extended_clOrdID(clOrdID)

            limit_order = pb.LimitOrder(
                token=self.token,
                clOrdID=extended_clOrdID,
                side=side,
                securityID=securityID,
                quantity=quantity,
                price=price,
                timeInForce=timeInForce,
                expireTime=expireTime,
                settlType=settlType,
                account=account,
                display=display
            )
            message = pb.Message(
                messageType=pb.MessageType.LIMIT_ORDER,
                limitOrder=limit_order
            )
            buffer = message.SerializeToString()
            self.send_order(buffer)
        except Exception as e:
            print(f"Error creating limit order: {e}")

    def send_limit_replace(self, clOrdID, origClOrdID, quantity, price, expireTime, account, display):
        try:
            extended_clOrdID = self.generate_extended_clOrdID(clOrdID)

            limit_replace = pb.LimitReplace(
                token=self.token,
                clOrdID=extended_clOrdID,
                origClOrdID=origClOrdID,
                quantity=quantity,
                price=price,
                expireTime=expireTime,
                account=account,
                display=display
            )
            message = pb.Message(
                messageType=pb.MessageType.LIMIT_REPLACE,
                limitReplace=limit_replace
            )
            buffer = message.SerializeToString()
            self.send_order(buffer)
        except Exception as e:
            print(f"Error creating limit replace: {e}")

    def send_limit_cancel(self, clOrdID, origClOrdID):
        try:
            extended_clOrdID = self.generate_extended_clOrdID(clOrdID)

            limit_cancel = pb.LimitCancel(
                token=self.token,
                clOrdID=extended_clOrdID,
                origClOrdID=origClOrdID
            )
            message = pb.Message(
                messageType=pb.MessageType.LIMIT_CANCEL,
                limitCancel=limit_cancel
            )
            buffer = message.SerializeToString()
            self.send_order(buffer)
        except Exception as e:
            print(f"Error creating limit cancel: {e}")

    def generate_extended_clOrdID(self, clOrdID):
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        extended_clOrdID = f"{clOrdID}-{suffix}"
        return extended_clOrdID[:20]
