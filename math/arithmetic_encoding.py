from decimal import Decimal

class ArithmeticEncoding:
    def __init__(self, frequency_table):
        self.probability_table = self.__get_probability_table(frequency_table)

    def __get_probability_table(self, frequency_table):
        total_frequency = sum(list(frequency_table.values()))

        self.probability_table = {}
        for key, value in frequency_table.items():
            self.probability_table[key] = value/total_frequency

        return self.probability_table

    def get_encoded_value(self, encoder):
        last_stage = list(encoder[-1].values())
        last_stage_values = []
        for sublist in last_stage:
            for element in sublist:
                last_stage_values.append(element)

        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)

        return (last_stage_min + last_stage_max)/2

    def process_stage(self, stage_min, stage_max):
        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(self.probability_table.items())):
            term = list(self.probability_table.keys())[term_idx]
            term_prob = Decimal(self.probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        
        return stage_probs

    def encode(self, msg):
        encoder = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for msg_term_idx in range(len(msg)):
            stage_probs = self.process_stage(stage_min, stage_max)

            msg_term = msg[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            encoder.append(stage_probs)

        stage_probs = self.process_stage(stage_min, stage_max)
        encoder.append(stage_probs)

        encoded_msg = self.get_encoded_value(encoder)

        return encoder, encoded_msg

    def decode(self, encoded_msg):
        decoder = []
        decoded_msg = ""
        msg_length = len(encoded_msg)

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for idx in range(msg_length):
            stage_probs = self.process_stage(stage_min, stage_max)

            for msg_term, value in stage_probs.items():
                if encoded_msg >= value[0] and encoded_msg <= value[1]:
                    break

            decoded_msg = decoded_msg + msg_term
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            decoder.append(stage_probs)

        stage_probs = self.process_stage(stage_min, stage_max)
        decoder.append(stage_probs)

        return decoder, decoded_msg

if __name__ == "__main__":
    table = {'L': 3, 'o': 136, 'r': 173, 'e': 368, 'm': 155, ' ': 551, 'i': 324, 'p': 61, 's': 259, 'u': 276, 'd': 82, 'l': 169, 't': 264, 'a': 232, ',': 54, 'c': 128, 'n': 172, 'g': 40, '.': 69, 'U': 1, 'q': 40, 'I': 6, 'v': 39, 'E': 3, 'D': 9, 'Q': 4, 'b': 36, 'f': 28, 'F': 4, 'h': 19, 'V': 4, 'x': 10, 'M': 7, 'A': 4, 'P': 7, 'j': 2, 'S': 5, '\n': 8, 'O': 1, 'N': 7, 'C': 4}
    coder = ArithmeticEncoding(table)

    decoded = coder.decode("hello")

    print(decoded)