from time import sleep

from smartcard.scard import *
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest

def get():
    try:
        cardType = AnyCardType()
        cardRequest = CardRequest( timeout=0, cardType=cardType )
        cardService = cardRequest.waitforcard()

        deviceId = cardService.connection.getReader()

        pos = int(deviceId[-1])

        #get the unique id of nfc card
        hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)

        hresult==SCARD_S_SUCCESS

        hresult, readers = SCardListReaders(hcontext, [])

        len(readers)>0

        reader = readers[pos]

        hresult, hcard, dwActiveProtocol = SCardConnect(
        hcontext,
        reader,
        SCARD_SHARE_SHARED,
        SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)


        hresult, cardId = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0xCA,0x00,0x00,0x00])

        uid = ''
        for value in cardId:
            val = hex(value).replace('0x', '').upper()
            if len(val) == 1: val = '0' + val

            if cardId.index(value) == (len(cardId) - 1):
                separator = ""
            else:
                separator = " - "
            uid += f"{val}{separator}"

        return uid
    except Exception:
        return "No ID detected!"