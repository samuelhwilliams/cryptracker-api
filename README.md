# Cryptracker

Provides a trivial endpoint to (roughly) convert cryptocurrencies to fiat currencies.

Really quite an abysmal implementation, but it will do for now.

Requires a user and group called 'cryptracker' to use the existing Apache2 config in `deploy`.


## Endpoint...s?
`/convert`:
* Parameters:
  * Required:
    * source: source cryptocurrency code (e.g. BTC)
    * amount: number of coins (e.g. 1.00)
    * target: target fiat currency code (e.g. GBP)
  * Optional:
    * paid:   the amount paid in the target currency when the source cryptocurrency was purchased (e.g. 100.00)
* Returns:
  * Dict:
    * :wq

