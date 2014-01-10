import events
import scenes


class SceneTemplateRegistry():
    def __init__(self):
        self.sceneTemplates = []

    def __call__(self, sceneTemplateMethod):
        self.sceneTemplates.append(sceneTemplateMethod)

    def register(self, gameState):
        for s in self.sceneTemplates:
            s(gameState)
            
sceneTemplate = SceneTemplateRegistry()

def addSceneTemplates(gameState):
    sceneTemplate.register(gameState)

# TODO: put all the addEvents into a method that gets called to generate the actual scene, instead of the scene template being used as a scene

@sceneTemplate
def imperialCourt(gameState):        
    ns = scenes.Scene()
    ns.name = 'Imperial Court'
    def isValid(gameState):
        return gameState.location == ns.name
    ns.isValid = isValid
    def score(gameState):
        return 0
    ns.score = score
    ns.addEvent(events.Narration("The Emperor regards you down his long nose as you kneel before him. As the pause extends, you begin to feel uncomfortable."))
    ns.addEvent(events.Say(gameState.emperor, "What was your name again?"))
    ns.addEvent(events.GetUserText("Type your name and press Enter", lambda text : setattr(gameState.player, 'name', text)))
    ns.addEvent(events.Say(gameState.player, "", lambda : "I am " + gameState.player.name + ", Emperor."))
    ns.addEvent(events.Say(gameState.emperor, "Ah yes, I'm told you saved my life by killing an assassin at the parade last week."))
    ns.addEvent(events.Say(gameState.emperor, "And if I'm not mistaken, the same Imperial agent who ended the siege of Ilsar, and more recently found the Tantoma Scrolls. The Arcanum tells me they are learning much from them."))
    ns.addEvent(events.GetUserChoice("Do you ...", [events.GetUserChoice.Choice('Stay Silent'), events.GetUserChoice.Choice('Speak up', lambda : print("spoke"))]))
    ns.addEvent(events.Say(gameState.emperor, "The Empire is repaying your loyalty and resourcefulness by elevating you to nobility. Perhaps others will be inspired by your success."))
    ns.addEvent(events.Say(gameState.emperor, "", lambda : "Arise Dominus " + gameState.player.name + "."))
    ns.addEvent(events.Say(gameState.emperor, "Now there is the matter of a domain to live on. The Caldar region requires a new Dominus urgently, as it has been several months since Dominus Tenjin disappeared."))
    ns.addEvent(events.Say(gameState.emperor, "It is on the Eastern border of the Empire, not entirely civilised, but I believe it will suit your adventurous spirit! I shall send an advisor with you to help you learn the ways of a Dominus."))
    ns.addEvent(events.Say(gameState.emperor, "You will leave on tomorrow's Eastern railvan."))
    ns.addEvent(events.Narration("Nobility! All of your descendants will bear this status. If you have any, that is. The thought of governing a domain makes you a little nervous, but how hard can the life of a noble be? You've definitely survived worse."))
    def onExit(gameState):
        gameState.location = 'Arinna Central Railvan Station'
    ns.onExit = onExit
    gameState.addSceneTemplate(ns)

@sceneTemplate
def railvanStation(gameState):
    ns = scenes.Scene()    
    ns.name = 'Arinna Central Railvan Station'
    def isValid(gameState):
        return gameState.location == ns.name
    ns.isValid = isValid
    def score(gameState):
        return 0
    ns.score = score
    ns.addEvent(events.Narration("And so early in the morning, you push your way through the bustle of the capital to the central rail station, looking for your advisor. He is not hard to spot, surrounded by twenty Imperial guards."))
    ns.addEvent(events.Say(gameState.advisor, "", lambda : "Good morning " + gameState.player.name + "! I can see you haven't brought much apart from your weapons, but never fear, I have many books on a variety of subjects. We can also buy some clothes on the way."))
    ns.addEvent(events.Narration("Johan steps up into the first class railvan carriage being pushed in front of the engine, and you follow him. The troops pack into a van pulled behind, and the caravan jolts forward slowly gaining speed."))
    def onExit(gameState):
        gameState.location = 'Railvan to Hyree'
    ns.onExit = onExit
    gameState.addSceneTemplate(ns)
    