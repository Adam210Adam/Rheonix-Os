Dim Message, Speak
Message=MsgBox("Process C:\Users\Adam\Desktop\Render\Drive\Program Files (x86)\Render2.0InstallationEXESetupOS.exe Failed",2+16,"Render Respond Center")
If Message=vbRetry Then
    msss=MsgBox("Cannot Fix Problem It is a major Error and unexpected",0+16,"Render Respond Center") 
End If
Messages=MsgBox("Process C:\Users\Adam\Desktop\Render\config.json Failed With Code 1",2+16,"Render Respond Center") 
If Messages=vbRetry Then
    MSG=MsgBox("Sucsessfully Diagnosed config.json!",0+48,"Render Respond Center")
End If
