## Disconary
A discord and theasaurus term lookup bot.
Could be pointless, could be useful; I made this primarly just to try some things out :)

### Set up
For authenticated this bot with your Discord application token, you can either create a 
config.json file in the root directory of this project like so...
```json
{
  "token": "Your application token"
}
```

... Or just replace this bit of code with a string containing it:
```python
// From this
client.run(config.contents["token"])
// To this
client.run("Your application token")
```
