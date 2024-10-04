import asyncio
from  AsyncPayments.cryptoBot import AsyncCryptoBot
from decouple import config 
# https://github.com/I-ToSa-I/AsyncPayments


cryptobot = AsyncCryptoBot(config("CryptoBotToken"), False)


async def create_order(amount):
    order = await cryptobot.create_invoice(amount, currency_type="fiat", asset="RUB")
    print('CryptoBot: ', order.pay_url)


async def get_info(id):
    info = await cryptobot.get_invoices(invoice_ids=[str(id)], count=1)


# info_crypto_bot.amount
# info_crypto_bot.status
# for balance in balance_crypto_bot:
#        print(f"Доступно {balance.currency_code}: ", balance.available, f" (В холде: {balance.onhold})")