class Solution:
    def candy(self, ratings: List[int]) -> int:
        output = [1]*len(ratings)
        reversed_ratings = list(reversed(ratings))

        def candy_game(ratings, output):
            for i in range(len(ratings)-1):
                if ratings[i] > ratings[i+1]:
                    if output[i] > output[i+1]:
                        pass
                    else:
                        output[i] =  output[i] + 1
                elif ratings[i] == ratings[i+1]:
                    pass
                else:
                    if output[i+1] > output[i]:
                        pass
                    else:
                        output[i+1] =  output[i] + 1
            return output
        return sum(candy_game(reversed_ratings, list(reversed(candy_game(ratings,output)))))