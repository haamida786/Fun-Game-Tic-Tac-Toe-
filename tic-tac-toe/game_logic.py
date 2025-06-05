from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global game state (for simplicity)
board = [''] * 9
current_player = 'X'

def check_win(b, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global board, current_player
    data = request.get_json()
    cell = int(data['cell'])

    if board[cell] == '':
        board[cell] = current_player
        if check_win(board, current_player):
            result = f'Player {current_player} wins!'
            game_over = True
        elif '' not in board:
            result = 'It\'s a tie!'
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            result = f'Player {current_player}\'s turn'
            game_over = False
    else:
        result = 'Invalid move'
        game_over = False

    return jsonify(board=board, status=result, over=game_over)

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [''] * 9
    current_player = 'X'
    return jsonify(board=board, status="Player X's turn", over=False)

if __name__ == '__main__':
    app.run(debug=True)
