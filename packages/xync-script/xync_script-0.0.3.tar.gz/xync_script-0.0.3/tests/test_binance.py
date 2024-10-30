import logging
from xync_client.binance.sapi import Sapi
from xync_scripts.loader import BKEY, BSEC

logging.basicConfig(level=logging.DEBUG)


async def test_sapi():
    sapi = Sapi(BKEY, BSEC)
    pms = await sapi.get_pay_meths()
    assert len(pms), "SAPI isn't available"
