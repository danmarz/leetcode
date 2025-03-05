class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        # # Brute-force approach
        # current_energy = initialEnergy
        # current_experience = initialExperience
        # hours = 0
        # oponent = 0

        # while oponent < len(energy):
        #     if energy[oponent] < current_energy and experience[oponent] < current_experience:
        #         current_energy -= energy[oponent]
        #         current_experience += experience[oponent]
        #         oponent +=1
        #     else:
        #         if energy[oponent] >= current_energy:
        #             current_energy += 1
        #         elif experience[oponent] >= current_experience:
        #             current_experience += 1
        #         hours +=1

        # return hours

        # Elegant, efficient approach handling both constraints in different approaches
        total_training = 0

        # Energy required is sum of all opponents' energy + 1
        energy_required = sum(energy) + 1
        if initialEnergy < energy_required:
            total_training += energy_required - initialEnergy

        # Experience training (handled iteratively)
        current_experience = initialExperience
        for exp in experience:
            if current_experience <= exp:
                needed = (exp - current_experience) + 1
                total_training += needed
                current_experience += needed  # Training adds experience
            current_experience += exp  # Gain experience after defeating the opponent

        return total_training
