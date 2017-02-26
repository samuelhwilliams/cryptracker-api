# Cryptracker

Provides a trivial endpoint to (roughly) convert cryptocurrencies to fiat currencies.

Really quite an abysmal implementation, but it will do for now.

Requires a user and group called 'cryptracker' to use the existing Apache2 config in `deploy/`.


## Endpoint...s?
`/convert`:

* Parameters:
  * <string:source> - source cryptocurrency code (e.g. BTC)
  * <float:amount>  - number of coins (e.g. 1.00)
  * <string:target> - target fiat currency code (e.g. GBP)
  * Optional:
    * <float:paid>    - the amount paid in the target currency when the source cryptocurrency was purchased (e.g. 100.00)

* Returns
  * Dict:
    * <string:source>: <float:amount> - The number of cryptocurrency units passed in with the request.
    * <string:target>: <float:amount> - The amount of fiat currency the given cryptocurrency is worth (ROUGHLY).
    * "usd\_per\_coin": <float> - The value of 1 coin of the given cryptocurrency in USD.
    * Optional keys:
      * "change": <float> - The net change in value compared to the amount paid (if supplied).
      * "usd": <float> - The value of the cryptocurrency in USD (if USD is not the target currency).
      * "paid": <float> - The same as passed in (if supplied).
