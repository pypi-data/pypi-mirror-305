# -*- coding: utf-8 -*-
import requests
import json
import dateutil.parser
from .errors import ValidationError, AuthorizationError, ServiceError
import logging
_logger = logging.getLogger(__name__)

medios_pago = {
    'Webpay': 1,
    'Servipag': 2,
    'Klap': 3,
    'Onepay': 5,
    'Cryptocompra': 8,
    'Todos los medios': 9,
    'Mach': 15,
    "Transferencias bancarias vía Khipu": 22,
    "Chek": 25,
    'Webpay 3C': 130,
    "Webpay 6C": 131,
    "Webpay 6C": 131,
    "Webpay 12C": 132,
}


class BaseResponse(object):
    @classmethod
    def from_response(cls, response):
        data = json.loads(response.data.decode())
        _logger.info("res %s" %data)
        if data.get('token') or data.get('flowOrder'):
            return cls.from_data(data)
        else:
            if data.get('code'):
                raise ValidationError.from_data(data)
            if response.status_code == requests.codes.forbidden:
                err = AuthorizationError.from_data(data)
                raise err
            if response.status_code == requests.codes.service_unavailable:
                raise ServiceError.from_data(data)


class PaymentsResponse(BaseResponse):
    def __init__(self, payment_id, url, simplified_transfer_url,
        transfer_url, app_url, ready_for_terminal, token,
        receiver_id, conciliation_date, subject, amount, currency, status,
        payment_data, body, picture_url, receipt_url, return_url, cancel_url,
        notify_url, notify_api_version, expires_date, attachment_urls, bank,
        bank_id, payer_name, email, personal_identifier,
        bank_account_number, out_of_date_conciliation, transaction_id, custom,
        responsible_user_email, send_reminders, send_email, paymentMethod,
        code, message):
        self._payment_id = payment_id
        self._url = url
        self._simplified_transfer_url = simplified_transfer_url
        self._transfer_url = transfer_url
        self._app_url = app_url
        self._ready_for_terminal = ready_for_terminal
        self._token = token
        self._receiver_id = receiver_id
        self._conciliation_date = conciliation_date
        self._subject = subject
        self._amount = amount
        self._currency = currency
        self._status = status
        self._payment_data = payment_data
        self._body = body
        self._picture_url = picture_url
        self._receipt_url = receipt_url
        self._return_url = return_url
        self._cancel_url = cancel_url
        self._notify_url = notify_url
        self._notify_api_version = notify_api_version
        self._expires_date = expires_date
        self._attachment_urls = attachment_urls
        self._bank = bank
        self._bank_id = bank_id
        self._payer_name = payer_name
        self._email = email
        self._personal_identifier = personal_identifier
        self._bank_account_number = bank_account_number
        self._out_of_date_conciliation = out_of_date_conciliation
        self._transaction_id = transaction_id
        self._custom = custom
        self._responsible_user_email = responsible_user_email
        self._send_reminders = send_reminders
        self._send_email = send_email
        self._paymentMethod = paymentMethod
        self._code = code
        self._message = message

    @classmethod
    def from_data(cls, data):
        payment_data = data.get('paymentData', {})
        payment_method = None
        if payment_data and payment_data.get('media'):
            payment_method = medios_pago[payment_data['media']]

        conciliation_date = None
        if payment_data and payment_data.get('date'):
            conciliation_date = dateutil.parser.parse(payment_data.get('date'))
        expires_date = False #dateutil.parser.parse(data.get('expires_date'))

        return cls(data.get('flowOrder'), data.get('url'),
            data.get('simplified_transfer_url'), data.get('transfer_url'),
            data.get('app_url'), data.get('ready_for_terminal'),
            data.get('token'), data.get('receiver_id'),
            conciliation_date, data.get('subject'),
            data.get('amount'), data.get('currency'), data.get('status'),
            data.get('paymentData'), data.get('body'),
            data.get('picture_url'), data.get('receipt_url'),
            data.get('return_url'), data.get('cancel_url'),
            data.get('notify_url'), data.get('notify_api_version'),
            expires_date, data.get('attachment_urls'),
            data.get('bank'), data.get('bank_id'), data.get('payer_name'),
            data.get('email') or data.get('payer'), data.get('personal_identifier'),
            data.get('bank_account_number'),
            data.get('out_of_date_conciliation'), data.get('commerceOrder'),
            data.get('custom'), data.get('responsible_user_email'),
            data.get('send_reminders'), data.get('send_email'),
            data.get('paymentMethod', payment_method),
            data.get('code'),data.get('message'))

    @property
    def payment_id(self):
        """
        Identificador único del pago, es una cadena alfanumérica de 12 caracteres
        """
        return self._payment_id

    @property
    def url(self):
        """
        URL principal del pago, si el usuario no ha elegido previamente un
        método de pago se le muestran las opciones
        """
        return self._url

    @property
    def simplified_transfer_url(self):
        """
        URL de pago simplificado
        """
        return self._simplified_transfer_url

    @property
    def transfer_url(self):
        """
        URL de pago normal
        """
        return self._transfer_url

    @property
    def app_url(self):
        """
        URL para invocar el pago desde un dispositivo móvil usando la APP de
        khipu
        """
        return self._app_url

    @property
    def ready_for_terminal(self):
        """
        Es 'true' si el pago ya cuenta con todos los datos necesarios para abrir
        directamente la aplicación de pagos khipu
        """
        return self._ready_for_terminal

    @property
    def token(self):
        """
        Cadena de caracteres alfanuméricos que identifican unicamente al pago,
        es el identificador que el servidor de khipu enviará al servidor del
        comercio cuando notifique que un pago está conciliado
        """
        return self._token

    @property
    def receiver_id(self):
        """
        Identificador único de una cuenta de cobro
        """
        return self._receiver_id

    @property
    def conciliation_date(self):
        """
        Fecha y hora de conciliación del pago.
        """
        return self._conciliation_date

    @property
    def subject(self):
        """
        Motivo del pago
        """
        return self._subject

    @property
    def amount(self):
        """
        """
        return self._amount

    @property
    def currency(self):
        """
        El código de moneda en formato ISO-4217
        """
        return self._currency

    @property
    def status(self):
        """
        Estado del pago, puede ser 'pending' (el pagador aún no comienza a
        pagar), 'verifying' (se está verificando el pago) o 'done', cuando el
        pago ya está confirmado
        """
        return self._status

    @property
    def payment_data(self):
        """
        Detalle del estado del pago, 'pending' (el pagadon aún no comienza a
        pagar), 'normal' (el pago fue verificado y fue cancelado por algún medio
        de pago estandar), 'marked-paid-by-receiver' (el cobrador marco el cobro
        como pagado por otro medio), 'rejected-by-payer' (el pagador declaró que
        no pagará), 'marked-as-abuse' (el pagador declaró que no pagará y que el
        cobro fue no solicitado) y 'reversed' (el pago fue anulado por el
        comercio, el dinero fue devuelto al pagador).
        """
        return self._payment_data

    @property
    def body(self):
        """
        Detalle del cobro
        """
        return self._body

    @property
    def picture_url(self):
        """
        URL de cobro
        """
        return self._picture_url

    @property
    def receipt_url(self):
        """
        URL del comprobante de pago
        """
        return self._receipt_url

    @property
    def return_url(self):
        """
        URL donde se redirige al pagador luego que termina el pago
        """
        return self._return_url

    @property
    def cancel_url(self):
        """
        URL donde se redirige al pagador luego de que desiste hacer el pago
        """
        return self._cancel_url

    @property
    def notify_url(self):
        """
        URL del webservice donde se notificará el pago
        """
        return self._notify_url

    @property
    def notify_api_version(self):
        """
        Versión de la api de notificación
        """
        return self._notify_api_version

    @property
    def expires_date(self):
        """
        Fecha de expiración del pago.
        """
        return self._expires_date

    @property
    def attachment_urls(self):
        """
        URLs de archivos adjuntos al pago
        """
        return self._attachment_urls

    @property
    def bank(self):
        """
        Nombre del banco seleccionado por el pagador
        """
        return self._bank

    @property
    def bank_id(self):
        """
        Identificador del banco seleccionado por el pagador
        """
        return self._bank_id

    @property
    def payer_name(self):
        """
        Nombre del pagador
        """
        return self._payer_name

    @property
    def email(self):
        """
        Correo electrónico del pagador
        """
        return self._email

    @property
    def personal_identifier(self):
        """
        Identificador personal del pagador
        """
        return self._personal_identifier

    @property
    def bank_account_number(self):
        """
        Número de cuenta bancaria del pagador
        """
        return self._bank_account_number

    @property
    def out_of_date_conciliation(self):
        """
        Es 'True' si la conciliación del pago fue hecha luego de la fecha de
        expiración
        """
        return self._out_of_date_conciliation

    @property
    def transaction_id(self):
        """
        String Identificador del pago asignado por el cobrador
        """
        return self._transaction_id

    @property
    def custom(self):
        """
        String Campo genérico que asigna el cobrador al momento de hacer el pago
        """
        return self._custom

    @property
    def responsible_user_email(self):
        """
        String Correo electrónico de la persona responsable del pago
        """
        return self._responsible_user_email

    @property
    def send_reminders(self):
        """
        Es 'True' cuando este es un cobro por correo electrónico y khipu enviará
        recordatorios
        """
        return self._send_reminders

    @property
    def send_email(self):
        """
        Es 'True' cuando khipu enviará el cobro por correo electrónico
        """
        return self._send_email

    @property
    def paymentMethod(self):
        """
        Método de pago usado por el pagador, puede ser 'regular_transfer'
        (transferencia normal), 'simplified_transfer' (transferencia
        simplificada) o 'not_available' (para un pago marcado como realizado por
        otro medio por el cobrador).
        """
        return self._paymentMethod

    @property
    def code(self):
        """
        Código de Error
        """
        return self._code

    @property
    def message(self):
        """
        Mensage de Error
        """
        return self._message


class PaymentsCreateResponse(BaseResponse):
    def __init__(self, payment_id, url, token, simplified_transfer_url,
        transfer_url, app_url, ready_for_terminal):
        self._payment_id = payment_id
        self._url = url
        self._simplified_transfer_url = simplified_transfer_url
        self._transfer_url = transfer_url
        self._app_url = app_url
        self._ready_for_terminal = ready_for_terminal
        self._token = token

    @classmethod
    def from_data(cls, data):
        return cls(data.get('payment_id'), data.get('url'), data.get('token'),
            data.get('simplified_transfer_url'), data.get('transfer_url'),
            data.get('app_url'), data.get('ready_for_terminal'))

    @property
    def payment_id(self):
        """
        Identificador único del pago, es una cadena alfanumérica de 12
        caracteres
        """
        return self._payment_id

    @property
    def url(self):
        """
        URL principal del pago, si el usuario no ha elegido previamente un
        método de pago se le muestran las opciones
        """
        return self._url

    @property
    def token(self):
        """
        TOKEN principal del pago, si el usuario no ha elegido previamente un
        método de pago se le muestran las opciones
        """
        return self._token

    @property
    def simplified_transfer_url(self):
        """
        URL de pago simplificado
        """
        return self._simplified_transfer_url

    @property
    def transfer_url(self):
        """
        URL de pago normal
        """
        return self._transfer_url

    @property
    def app_url(self):
        """
        URL para invocar el pago desde un dispositivo móvil usando la APP de
        khipu
        """
        return self._app_url

    @property
    def ready_for_terminal(self):
        """
        Es 'True' si el pago ya cuenta con todos los datos necesarios para abrir
        directamente la aplicación de pagos khipu
        """
        return self._ready_for_terminal


class ReceiversCreateResponse(BaseResponse):
    def __init__(self, receiver_id, secret):
        self._receiver_id = receiver_id
        self._secret = secret

    @classmethod
    def from_data(cls, data):
        return cls(data.get('receiver_id'), data.get('secret'))

    @property
    def receiver_id(self):
        """
        Identificador único de la cuenta de cobro
        """
        return self._receiver_id

    @property
    def secret(self):
        """
        Llave secreta de la cuenta de cobro, se usa para firmar todas las
        peticiones
        """
        return self._secret


class BanksResponse(BaseResponse):
    def __init__(self, banks):
        self._banks = banks

    @classmethod
    def from_data(cls, data):
        #banks = [BankItem.from_data(i) for i in data.get('banks')]
        return cls(banks.get('banks'))

    @property
    def banks(self):
        """
        Arreglo de BankItems
        """
        return self._banks


class SuccessResponse(BaseResponse):
    def __init__(self, message):
        self._message = message

    @classmethod
    def from_data(cls, data):
        return cls(data['message'])

    @property
    def message(self):
        """
        Mensaje a desplegar al usuario
        """
        return self._message
