Dim Message, Speak
Message="M Mode Selected"

Set Speak=CreateObject("sapi.spvoice")
Speak.Speak Message