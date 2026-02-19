import time as t
import os
try:
    from rich import print
    import pyfiglet
    import pyautogui as s
except ModuleNotFoundError:
    print("Required modules not found. Installing...")
    os.system("python -m pip install rich pyfiglet pyautogui")
    from rich import print
    import pyfiglet
    import pyautogui as s
a = 1
print("""[bold white]Enter Your Os Name[/bold white] 
1. [bold blue]Windows[/bold blue]
2. [bold red]Linux[/bold red]
""")

osname = input("Os Name (1/2) : ")
t.sleep(1)
if osname == "1":
   print("[bold white]This tool will open WhatsApp on your device and automatically send messages through your logged-in account. Do you give permission to proceed? (y/n) : [/bold white]")
   t.sleep(1)
   permission = input("Answer : ")
   t.sleep(0.5)
   tool = input("Do You Want To Run The Tool  (y/n) : ")
   t.sleep(1) 
   print("[bold white]Processing....[/bold white]")
   t.sleep(1)
   if tool.lower() == "y" and permission.lower() == "y": 
     print("[bold white]Running...[/bold white]")
     t.sleep(2)
     os.system("cls")
     t.sleep(0.5)
     nametool = pyfiglet.figlet_format("WebChat Automator", font="small")
     print(f"[bold bright_green]{nametool}[/bold bright_green]")
     t.sleep(3)
     print("[bold red]This tool is made for educational and fun purposes only To Prank Your Freind. Do not misuse it or disturb anyone. [/bold red]")
     t.sleep(3)
     print("""[bold blue]Made By : Akshat Rajput[/bold blue]                                             [bold white]Version : Windows v1.0[/bold white]                                                                                                                                                                           """)
     t.sleep(2)
     print("[bold cyan]Enter The Target Phone Number Ex : +91 xxxxxxxxx : [/bold cyan]")
     t.sleep(1)
     targetnamewhatsappwindows =input("Number : ")
     t.sleep(1)
     print("[bold cyan]Enter The Message That You Want To Spam [/bold cyan]")
     t.sleep(1)
     message1 = input("Message : ")
     t.sleep(1)
     print("[bold cyan]Enter How much Time Did You Spam The Messgae[/bold cyan]")
     ktinibaar1 = int(input("Time : "))
     t.sleep(1)
     print("[bold white]Running....[/bold white]")
     t.sleep(2)
     print("[bold white]Please Do Not Touch The Screen Tool Is Running...[/bold white]")
     t.sleep(3)
     s.press("win")
     t.sleep(1)
     s.write("Whatsapp",interval=0.2)
     s.press("enter")
     t.sleep(3)
     s.hotkey("ctrl","f")
     t.sleep(0.5)
     s.write(targetnamewhatsappwindows,interval=0.2)
     s.press("enter")
     t.sleep(1.5)
     i = 1 
     while(i <= ktinibaar1):
        s.write(message1)
        s.press("enter")
        print("[bold bright_green]Message Sent Successfully![/bold bright_green]")
        i = i+1
   else:
       print("[bold white]Thanks For Using It[/bold white]")
elif osname == "2":
    print("[bold white]This tool will open WhatsApp on your device and automatically send messages through your logged-in account. Do you give permission to proceed? (y/n) : [/bold white]")
    t.sleep(1)
    permission2 = input("Answer : ")
    t.sleep(0.5)
    tool2 = input("Do You Want To Run The Tool  (y/n) : ")
    t.sleep(1)
    print("[bold white]Processing....[/bold white]")
    t.sleep(1)
    if tool2.lower() == "y" and permission2.lower() == "y": 
       print("[bold white]Running...[/bold white]")
       t.sleep(2)
       os.system("clear")
       t.sleep(0.5)
       nametool = pyfiglet.figlet_format("WebChat Automator", font="small")
       print(f"[bold bright_green]{nametool}[/bold bright_green]")
       t.sleep(3)
       print("[bold red]This tool is made for educational and fun purposes only. Do not misuse it or disturb anyone. 💻✨[/bold red]")
       t.sleep(3)
       print("""[bold blue]Made By : Akshat Rajput[/bold blue]                                             [bold white]Version : Linux v1.0[/bold white]                                                                                                                                                                     .""")
       text = "[bold red]Requirements For Running This Tool On Linux[/bold red]"
       print(text.center(100))
       t.sleep(2)
       print("""[bold green]   -To run this tool on Linux, Firefox must be installed on the system,You must be
                         logged in to WhatsApp Web before running the tool.[/bold green]  """)
       t.sleep(3)
       linux = input("Have you read and completed all the requirements And You Also Run this Tool? (y/n): ")
       t.sleep(1)
       print("[bold white]Processing...[/bold white]")
       t.sleep(2)
       if linux == "y":
          print("[bold white]Running....[/bold white]")
          t.sleep(2)
          print("[bold cyan]Enter The Target Phone Number Ex : +91 xxxxxxxxx : [/bold cyan]")
          t.sleep(1)
          targetnamewhatsapp =input("Number : ")
          t.sleep(1)
          print("[bold cyan]Enter The Message That You Want To Spam [/bold cyan]")
          t.sleep(1)
          message = input("Message : ")
          t.sleep(1)
          print("[bold cyan]Enter How much Time Did You Spam The Messgae[/bold cyan]")
          ktinibaar = int(input("Time : "))
          t.sleep(1)
          print("[bold white]Running....[/bold white]")
          t.sleep(2)
          print("[bold white]Please Do Not Touch The Screen Tool Is Running...[/bold white]")
          t.sleep(3)
          os.system("firefox https://web.whatsapp.com")
          t.sleep(1)
          s.press("enter")
          t.sleep(15)
          s.hotkey("ctrl","f")
          t.sleep(0.5)
          s.write(targetnamewhatsapp,interval=0.2)
          s.press("enter")
          t.sleep(1.5)
          i = 1 
          while(i <= ktinibaar):
             s.write(message)
             s.press("enter")
             print("[bold bright_green]Message Sent Successfully![/bold bright_green]")
             i = i+1
       elif linux == "n":
          print("Please complete the requirements first ❗")
    else:
       print("[bold white]Thanks For Using It[/bold white]")

