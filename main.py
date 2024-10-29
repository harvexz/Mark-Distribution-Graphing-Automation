import random
import matplotlib.pyplot as plt
from collections import Counter

class QuizSimulator:
    def __init__(self, num_questions=20, num_options=4, knowledge_shift=0):
        """
        Initializes the QuizSimulator with the number of questions, answer options,
        + knowledge shift to simulate prior knowledge

        :param num_questions: Num of questions in quiz
        :param num_options: Num of possible answers
        :param knowledge_shift: Min num of questions assumed correct due to revision
        """
        self.num_questions = num_questions
        self.num_options = num_options
        self.knowledge_shift = knowledge_shift

    def simulate_participant_score(self):
        """
        Simulates the quiz for a single participant by generating random answers and
        counting the number of correct answers

        :return: The score of the participant, adjusted by knowledge shift
        """
        correct_answers = sum(random.randint(1, self.num_options) == 4 for _ in range(self.num_questions))
        # Apply knowledge shift to represent prior knowledge (e.g., assuming participant knows some answers)
        return min(self.num_questions, correct_answers + self.knowledge_shift)

class GradeDistribution:
    def __init__(self):
        """
        Initializes the GradeDistribution to store scores from multiple participants
        """
        self.scores = []

    def add_score(self, score):
        """
        Appends a participant's score to the list of scores

        :param score: The score of a single participant
        """
        self.scores.append(score)

    def calculate_distribution(self):
        """
        Calculates the frequency distribution of scores

        :return: A dictionary with score as key and frequency as value
        """
        return dict(Counter(self.scores))

class QuizAnalyzer:
    def __init__(self, num_participants=1000, knowledge_shift=0):
        """
        Initializes the QuizAnalyzer, which manages the simulation and analysis of the quiz results

        :param num_participants: Total number of participants taking the quiz
        :param knowledge_shift: The number of questions assumed to be known by participants
        """
        self.num_participants = num_participants
        self.knowledge_shift = knowledge_shift
        self.quiz_simulator = QuizSimulator(knowledge_shift=knowledge_shift)
        self.grade_distribution = GradeDistribution()

    def run_simulation(self):
        """
        Runs the quiz simulation for a defined number of participants and collects scores
        """
        for _ in range(self.num_participants):
            score = self.quiz_simulator.simulate_participant_score()
            self.grade_distribution.add_score(score)

    def plot_distribution(self):
        """
        Plots the distribution of quiz scores
        """
        distribution = self.grade_distribution.calculate_distribution()
        scores, frequencies = zip(*sorted(distribution.items()))

        plt.figure(figsize=(10, 6))
        plt.bar(scores, frequencies, color='skyblue', edgecolor='black')
        plt.xlabel('Score (Number of Correct Answers)')
        plt.ylabel('Frequency')
        plt.title(f'Distribution of Scores for {self.num_participants} Participants\n'
                  f'(with Knowledge Shift of {self.knowledge_shift})')
        plt.xticks(range(0, self.quiz_simulator.num_questions + 1))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def analyze(self):
        """
        Runs the full simulation and generates the distribution graph
        """
        print("* Starting simulation...")
        self.run_simulation()
        print("* Simulation complete. Displaying distribution graph...")
        self.plot_distribution()

if __name__ == "__main__":
    num_participants = 1000
    knowledge_shift = 4     # change for accepted correct questions...

    # simulate and analyze quiz results
    print("Beginning")
    analyzer = QuizAnalyzer(num_participants=num_participants, knowledge_shift=knowledge_shift)
    analyzer.analyze()
