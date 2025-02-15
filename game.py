import imgui
import numpy as np
from utils.graphics import Object, Camera, Shader
from assets.shaders.shaders import object_shader
from imgui.integrations.glfw import GlfwRenderer
import assets.objects.objects as assets

class Game:
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.state = "menu"
        self.camera = Camera(height, width)
        self.shaders = [Shader(object_shader['vertex_shader'], object_shader['fragment_shader'])]
        self.lives = 5
        self.backgrounds = []
        self.player = [Object(self.shaders[0], assets.playerProps), 
                       Object(self.shaders[0], assets.playerProps), 
                       Object(self.shaders[0], assets.playerProps)]
        self.coins_forest = [Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                      ]
        
        self.coins_river = [Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                ]

        self.coins_space = [Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                ]
        self.trees = [Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      Object(self.shaders[0], {**assets.treeProps, 'position': assets.random_position()}),
                      ]
        self.planets = [Object(self.shaders[0], assets.planet1Props),
                        Object(self.shaders[0], assets.planet2Props),
                        Object(self.shaders[0], assets.planet3Props),
                        ]
        self.clouds = [Object(self.shaders[0], assets.cloud1Props),
                       Object(self.shaders[0], assets.cloud2Props),
                       ]
        self.logs = [Object(self.shaders[0], {**assets.logProps, 'position': np.array([-350, 250, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([-250, -150, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([-150, 150, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([-50, 0, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([50, -160, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([150, -250, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([250, 40, 0])}),
                     Object(self.shaders[0], {**assets.logProps, 'position': np.array([350, 140, 0])}),                     
                     ]

        imgui.create_context()
        self.renderer = GlfwRenderer(window)

    def ProcessFrame(self, inputs, time): #have to update object based on inputs
        imgui.new_frame()

        if self.state == "menu":
            self.show_menu()
            self.lives = 5

        elif self.state == "forest_biome":
            self.show_forest_biome()

        elif self.state == "river_biome":
            self.show_river_biome()

        elif self.state == "space_biome":
            self.show_space_biome()

        elif self.state == "victory_forest":
            self.show_victory_forest()

        elif self.state == "victory_river":
            self.show_victory_river()

        elif self.state == "victory_space":
            self.show_victory_space()

        elif self.state == "defeat":
            self.defeat_screen()

        imgui.render()
        self.renderer.render(imgui.get_draw_data())

        if self.state == "menu":
            self.backgrounds = [Object(self.shaders[0], assets.menuProps)]
            # udpate camera matrix in shaders
            for shader in self.shaders:
                self.camera.Update(shader)

            # draw objects
            for cloud in self.clouds:
                cloud.Draw()
            for bg in self.backgrounds:
                bg.Draw()

        elif self.state == "victory_forest" or self.state == "victory_river" or self.state == "victory_space":
            self.backgrounds = [Object(self.shaders[0], assets.menuProps)]
            # udpate camera matrix in shaders
            for shader in self.shaders:
                self.camera.Update(shader)

            # draw objects
            for cloud in self.clouds:
                cloud.Draw()
            for bg in self.backgrounds:
                bg.Draw()

        elif self.state == "defeat":
            self.backgrounds = [Object(self.shaders[0], assets.defeatProps)]
            # udpate camera matrix in shaders
            for shader in self.shaders:
                self.camera.Update(shader)

            # draw objects
            for bg in self.backgrounds:
                bg.Draw()

        elif self.state == "forest_biome":
            self.backgrounds = [Object(self.shaders[0], assets.forestProps)]
            # update moving objects based on inputs
            self.player[0].properties["velocity"] = np.array([0,0,0], dtype=np.float32)
            if "W" in inputs:
                self.player[0].properties["velocity"][1] = self.player[0].properties["sens"]
            if "S" in inputs:
                self.player[0].properties["velocity"][1] = -self.player[0].properties["sens"]
            if "A" in inputs:
                self.player[0].properties["velocity"][0] = -self.player[0].properties["sens"]
            if "D" in inputs:
                self.player[0].properties["velocity"][0] = self.player[0].properties["sens"]
        
            self.player[0].properties["position"] += self.player[0].properties["velocity"] * time["deltaTime"]

            for coin in self.coins_forest:
                player_position = self.player[0].properties["position"]
                coin_position = coin.properties["position"]
            
                distance = np.linalg.norm(player_position - coin_position)

                if distance < 20:
                    print("Coin Collected!")
                    self.coins_forest.remove(coin)

            if(len(self.coins_forest) == 0):
                self.state = "victory_forest"

            for tree in self.trees:
                player_position = self.player[0].properties["position"]
                tree_position = tree.properties["position"]
            
                distance = np.linalg.norm(player_position - tree_position)

                if distance < 20:
                    print("TREE COLLISION!")
                    self.player[0].properties["position"] = np.array([-480, 0, 0], dtype = np.float32)
                    self.lives = self.lives - 1

            if self.lives == 0:
                self.state = "defeat"


            # udpate camera matrix in shaders
            for shader in self.shaders:
                self.camera.Update(shader)

            # draw objects
            self.player[0].Draw()
            for tree in self.trees:
                tree.Draw()
            for coin in self.coins_forest:
                coin.Draw()
            for bg in self.backgrounds:
                bg.Draw()

        elif self.state == "river_biome":
            self.backgrounds = [Object(self.shaders[0], assets.riverProps)]
            # update moving objects based on inputs
            self.player[1].properties["velocity"] = np.array([0,0,0], dtype=np.float32)
            if "W" in inputs:
                self.player[1].properties["velocity"][1] = self.player[1].properties["sens"]
            if "S" in inputs:
                self.player[1].properties["velocity"][1] = -self.player[1].properties["sens"]
            if "A" in inputs:
                self.player[1].properties["velocity"][0] = -self.player[1].properties["sens"]
            if "D" in inputs:
                self.player[1].properties["velocity"][0] = self.player[1].properties["sens"]
        
            self.player[1].properties["position"] += self.player[1].properties["velocity"] * time["deltaTime"]

            for coin in self.coins_river:
                player_position = self.player[1].properties["position"]
                coin_position = coin.properties["position"]
            
                distance = np.linalg.norm(player_position - coin_position)

                if distance < 20:
                    print("Coin Collected!")
                    self.coins_river.remove(coin)

            for log in self.logs:
                player_position = self.player[1].properties["position"]
                log_position = log.properties["position"]
            
                distance = np.linalg.norm(player_position - log_position)

                if distance < 3:
                    self.player[1].properties["position"] = log.properties["position"] + np.array([0, 0, 0], dtype=np.float32)

            if(len(self.coins_river) == 0):
                self.state = "victory_river"

            # udpate camera matrix in shaders
            for shader in self.shaders:
                self.camera.Update(shader)

            # draw objects
            self.player[1].Draw()
            for log in self.logs:
                log.properties["position"][1] += log.properties["velocity"][1]

                if log.properties["position"][1] >= 300 or log.properties["position"][1] <= -300:
                    log.properties["velocity"] *= -1
                log.Draw()
            for coin in self.coins_river:
                coin.Draw()
            for bg in self.backgrounds:
                bg.Draw()

        elif self.state == "space_biome":
            self.backgrounds = [Object(self.shaders[0], assets.spaceProps)]
            # update moving objects based on inputs
            self.player[2].properties["velocity"] = np.array([0,0,0], dtype=np.float32)
            if "W" in inputs:
                self.player[2].properties["velocity"][1] = self.player[2].properties["sens"]
            if "S" in inputs:
                self.player[2].properties["velocity"][1] = -self.player[2].properties["sens"]
            if "A" in inputs:
                self.player[2].properties["velocity"][0] = -self.player[2].properties["sens"]
            if "D" in inputs:
                self.player[2].properties["velocity"][0] = self.player[2].properties["sens"]

            self.player[2].properties["position"] += self.player[2].properties["velocity"] * time["deltaTime"]

            for coin in self.coins_space:
                player_position = self.player[2].properties["position"]
                coin_position = coin.properties["position"]
            
                distance = np.linalg.norm(player_position - coin_position)

                if distance < 20:
                    print("Coin Collected!")
                    self.coins_space.remove(coin)

            if(len(self.coins_space) == 0):
                self.state = "victory_space"

            for planet in self.planets:
                player_position = self.player[2].properties["position"]
                planet_position = planet.properties["position"]
            
                distance = np.linalg.norm(player_position - planet_position)
                print(distance)
                if distance < planet.properties["radius"]:
                    print("PLANET COLLISION!")
                    self.player[2].properties["position"] = np.array([-480, 0, 0], dtype = np.float32)
                    self.lives = self.lives - 1

            if self.lives == 0:
                self.state = "defeat"


            # udpate camera matrix in shaders
            for shader in self.shaders:
                self.camera.Update(shader)

            # draw objects
            self.player[2].Draw()
            for planet in self.planets:
                # self.time_elapsed += 0.0001
                # planet.properties["position"][1] = planet.properties["initial_position"][1] + 300*np.sin(self.time_elapsed)
                planet.properties["position"][1] += planet.properties["velocity"][1]

                if planet.properties["position"][1] >= 250 or planet.properties["position"][1] <= -250:
                    planet.properties["velocity"] *= -1  # Flip direction

                planet.Draw()
            for coin in self.coins_space:
                coin.Draw()
            for bg in self.backgrounds:
                bg.Draw()


    def show_menu(self):
        imgui.set_next_window_position(400, 300, 0)
        imgui.begin("PORTAL ADVENTURER")
        imgui.text("Welcome to the Game!")

        if imgui.button("Start Game"):
            self.state = "forest_biome"

        if imgui.button("Quit"):
            print("Exiting game...")
            exit(0)

        imgui.end()

    def show_forest_biome(self):
        imgui.begin("Forest Biome")
        imgui.text_colored(f"Welcome to the Forest!", 0,1,0,1)
        imgui.text_wrapped("Don't collide into trees")
        imgui.text_colored("Lives: "+"<3 " * self.lives, 1,0,0,1)

        if imgui.button("Back to Menu"):
            self.state = "menu"
        if imgui.button("Next Level"):
            self.state = "river_biome"

        imgui.end()

    def show_river_biome(self):
        imgui.begin("River Biome")
        imgui.text_colored(f"Welcome to the River!", 0.000, 0.749, 1.000, 1)
        imgui.text_wrapped("Don't get trapped in the fishing net")
        imgui.text_colored("Lives: "+"<3 " * self.lives, 1,0,0,1)

        if imgui.button("Back to Menu"):
            self.state = "menu"
        if imgui.button("Next Level"):
            self.state = "space_biome"

        imgui.end()

    def show_space_biome(self):
        imgui.begin("Space Biome")
        imgui.text_colored(f"Welcome to Space!", 0.576, 0.439, 0.859, 1)
        imgui.text_wrapped("Beware of planets pulling you in")
        imgui.text_colored("Lives: "+"<3 " * self.lives, 1,0,0,1)

        if imgui.button("Back to Menu"):
            self.state = "menu"
        imgui.end()

    def show_victory_forest(self):
        imgui.set_next_window_position(400, 300, 0)
        imgui.begin("VICTORY !!!")
        imgui.text("Forest Level Complete")

        # re init coins and player position
        self.coins_forest = [Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
                ]
        self.player[0].properties["position"] = np.array([-480, 0, 0], dtype = np.float32)

        if imgui.button("Next Level"):
            self.state = "river_biome"

        if imgui.button("Back to Menu"):
            self.state = "menu"
        imgui.end()
        
    def show_victory_river(self):
        imgui.set_next_window_position(400, 300, 0)
        imgui.begin("VICTORY !!!")
        imgui.text("River Level Complete")

        # re init coins and player position
        self.coins_river = [Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
            Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
            Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
            ]
        self.player[1].properties["position"] = np.array([-480, 0, 0], dtype = np.float32)


        if imgui.button("Next Level"):
            self.state = "space_biome"

        if imgui.button("Back to Menu"):
            self.state = "menu"
        imgui.end()

    def show_victory_space(self):
        imgui.set_next_window_position(400, 300, 0)
        imgui.begin("VICTORY !!!")
        imgui.text("Space Level Complete")
        imgui.text("---Game Over---")

        # re init coins and player position
        self.coins_space = [Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
            Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
            Object(self.shaders[0], {**assets.coinProps, 'position': assets.random_position()}),
            ]
        self.player[2].properties["position"] = np.array([-480, 0, 0], dtype = np.float32)


        if imgui.button("Back to Menu"):
            self.state = "menu"
        if imgui.button("Quit"):
            print("Exiting game...")
            exit(0)
        imgui.end()

    def defeat_screen(self):
        imgui.set_next_window_position(400, 300, 0)
        imgui.begin("Defeat")
        imgui.text("YOU LOSE")

        if imgui.button("Play Again"):
            self.state = "menu"

        if imgui.button("Quit"):
            print("Exiting game...")
            exit(0)
        
        imgui.end()