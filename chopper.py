from playsound import playsound
from pystyle import Anime, Colorate, Colors, Center, System, Write
from gtts import gTTS



asciiart = """
    _______   .---.  .---.     ,-----.    .-------. .-------.     .-''-.  .-------.     
   /   __  \  |   |  |_ _|   .'  .-,  '.  \  _(`)_ \\  _(`)_ \  .'_ _   \ |  _ _   \    
  | ,_/  \__) |   |  ( ' )  / ,-.|  \ _ \ | (_ o._)|| (_ o._)| / ( ` )   '| ( ' )  |    
,-./  )       |   '-(_{;}_);  \  '_ /  | :|  (_,_) /|  (_,_) /. (_ o _)  ||(_ o _) /    
\  '_ '`)     |      (_,_) |  _`,/ \ _/  ||   '-.-' |   '-.-' |  (_,_)___|| (_,_).' __  
 > (_)  )  __ | _ _--.   | : (  '\_/ \   ;|   |     |   |     '  \   .---.|  |\ \  |  | 
(  .  .-'_/  )|( ' ) |   |  \ `"/  \  ) / |   |     |   |      \  `-'    /|  | \ `'   / 
 `-'`-'     / (_{;}_)|   |   '. \_/``".'  /   )     /   )       \       / |  |  \    /  
   `._____.'  '(_,_) '---'     '-----'    `---'     `---'        `'-..-'  ''-'   `'-'   
                                                                                        
                                                                            
"""

def init():
 System.Clear()
 System.Title("Chopper")
 System.Size(190, 50)
 Anime.Fade(text=Center.Center(asciiart), color=Colors.cyan_to_blue, mode=Colorate.Vertical, enter=True)

def main():
 System.Clear() 
 print('\n'*2)
 print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(asciiart)))
 print('\n'*3) 

 Write.Input("Chopper est une intelligence artificielle qui permet de transformer un texte en audio.", color=Colors.cyan_to_blue, interval=0.005)   
 print()

 ts = Write.Input("Entrer le texte :", color=Colors.cyan_to_blue, interval=0.005) 
 
 print()


 audio = 'audio.mp3'
 language = 'fr'

 if not ts.strip():
   Colorate.Error("Veuillez indiquez un texte")
   return

 sp = gTTS(text=ts, lang= language,)

 sp.save(audio)

 if ts.strip():
    Write.Input("Un fichier audio.mp3 contenant le texte vient d'être créer", color=Colors.cyan_to_blue, interval=0.005)

 return


print()

if __name__ == '__main__':
    init()
    while True:
       main()