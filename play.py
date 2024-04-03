import game
import tic
import keys

debug_board = game.np.array([
                        [0, 0, 0],
                        [0, 2, 0],
                        [0, 0, 0]
                        ])
GTTT = game.Game(n=10, target=4, DEBUG_STATE=None, DEBUG_PRINT=False)
# GTTT.play_game_API(agent=tic.minimax)
# print(tic.minimax(curr_game=GTTT, state=GTTT.initial_state))
GTTT.play_game(game_type="AIvAI", agents=[[tic.heuristics_alpha_beta_pruning], [tic.heuristics_alpha_beta_pruning]], first_player="X")

# debug_state = game.State(state=debug_board, score=0, turn='O', available_actions=GTTT.generate_actions(debug_board))
# print(GTTT.feature_center_control(debug_state, player='O'))
# print(tic.create_game(keys.API_KEY, keys.USER_ID, "1397", "1424", 5, 4))
