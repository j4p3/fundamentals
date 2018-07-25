import pdb

class Game():

    MAX_LIVES = 3
    RIDDLES = [
        {
            'question': 'riddle a q',
            'options': [
                'answer 1',
                'answer 2',
                'answer 3',
            ],
            'answer': 1,
        },
        {
            'question': 'riddle a q',
            'options': [
                'answer 1',
                'answer 2',
                'answer 3',
            ],
            'answer': 2,
        },
        {
            'question': 'riddle a q',
            'options': [
                'answer 1',
                'answer 2',
                'answer 3',
            ],
            'answer': 3,
        },
    ]
    CORRECT_MESSAGE = 'CORRECTAMUNDO! NEXT LEVEL:'
    INCORRECT_MESSAGE = 'CALAMITY! REMAINING LIVES:'

    def __init__(self):
        self.state = {
            'question': 0,
            'lives': self.MAX_LIVES,
        }

    def run(self):
        current_question = self.state.get('question', 0)
        options = self.RIDDLES[current_question]['options']
        options_prompt = ['%i) %s' % (i+1, v) for (i, v) in enumerate(options)]

        print('\n %s \n' % self.RIDDLES[current_question]['question'])
        for option in options_prompt:
            print(option)
        answer = input('> ')

        if int(answer) == self.RIDDLES[current_question]['answer']:
            current_question += 1
            self.state['question'] = current_question
            print('%s %i' % (self.CORRECT_MESSAGE, current_question))
        else:
            self.state['lives'] -= 1
            print('%s %i' % (self.INCORRECT_MESSAGE, self.state['lives']))

        if self.state['lives'] == 0:
            print('GAME OVER')
            return
        elif self.state['question'] > 2:
            print('VICTORY')
            return

        self.run()

game = Game()
game.run()

