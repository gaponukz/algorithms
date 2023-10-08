from decimal import Decimal


class ArithmeticEncoder:
    def __init__(self, frequency_table: dict[str, float]):
        self._probability_table = frequency_table

    def _get_encoded_value(self, encoder: list[dict[str, list[Decimal]]]) -> Decimal:
        last_stage = list(encoder[-1].values())
        last_stage_values: list[Decimal] = []

        for sublist in last_stage:
            for element in sublist:
                last_stage_values.append(element)

        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)

        return (last_stage_min + last_stage_max) / 2

    def _process_stage(
        self, stage_min: Decimal, stage_max: Decimal
    ) -> dict[str, list[Decimal]]:
        stage_probs: dict[str, list[Decimal]] = {}
        stage_domain = stage_max - stage_min

        for term_idx in range(len(self._probability_table.items())):
            term = list(self._probability_table.keys())[term_idx]
            term_prob = Decimal(self._probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob

        return stage_probs

    def encode(self, msg: str) -> Decimal:
        encoder: list[dict[str, list[Decimal]]] = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for msg_term_idx in range(len(msg)):
            stage_probs = self._process_stage(stage_min, stage_max)

            msg_term = msg[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            encoder.append(stage_probs)

        stage_probs = self._process_stage(stage_min, stage_max)
        encoder.append(stage_probs)

        encoded_msg = self._get_encoded_value(encoder)

        return encoded_msg

    def decode(self, encoded_msg: Decimal | float, msg_length: int) -> str:
        decoder = []
        decoded_msg = ""

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for __ in range(msg_length):
            stage_probs = self._process_stage(stage_min, stage_max)

            for msg_term, value in stage_probs.items():
                if encoded_msg >= value[0] and encoded_msg <= value[1]:
                    break

            decoded_msg = decoded_msg + msg_term
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            decoder.append(stage_probs)

        stage_probs = self._process_stage(stage_min, stage_max)
        decoder.append(stage_probs)

        return decoded_msg


if __name__ == "__main__":
    frequency_table = {"a": 0.5, "b": 0.25, "c": 0.25}
    coder = ArithmeticEncoder(frequency_table)

    encoded_msg = coder.encode("abca")
    print(encoded_msg)

    msg = coder.decode(encoded_msg, 4)
    print(msg)
