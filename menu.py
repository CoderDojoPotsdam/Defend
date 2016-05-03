# Create a menu
import bge

# create a menu
# 1: title 2: [["Name": "Python script"], ["Name": "Python script"]]
def create_menu(title, values):
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner
    bge.logic.sendMessage("mTitle", title)
    mData = ""
    
    for i in values:
        mData += i[0] + "|" + i[1] + "#"
    
    bge.logic.sendMessage("mData", mData)
    
    bge.logic.addScene("Menu")

if __name__ == "__main__":
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    title = cont.sensors["title"]
    data = cont.sensors["data"]
    
    if len(title.bodies) != 0:
        scene.objects["MenuTitle"].text = title.bodies[0]
        scene.objects["MenuTitle"].resolution = 8.0
    
    cr = 0
    if len(data.bodies) != 0:
        entries = data.bodies[0].split("#")
        for pair in entries:
            if "|" in pair:
                cr += 1
                obj = scene.addObject("MenuEntry", "Spawn")
                pos = obj.worldPosition
                obj.worldPosition = [pos[0], pos[1], pos[2] - 0.3 * cr]
                obj.text = pair.split("|")[0]
                obj.resolution = 8.0
                obj.worldScale = scene.objects["MenuEntry"].worldScale
                scene.addObject("Background_normal", obj)
                scene.addObject("Background_highlighted", obj)
  
    scene.objects["Black"].visible = False
