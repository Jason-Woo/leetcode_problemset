class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify(line, width, maxWidth):
            if len(line) == 1:
                return line[0] + ' ' * (maxWidth - width)
            else:
                spaces = maxWidth - width
                locations = len(line) - 1
                assign = locations * [spaces // locations]
                for i in range(spaces % locations):
                    assign[i] += 1
                s = ''
                for i in range(locations):
                    s += line[i] + assign[i] * ' '
                s += line[-1]
                return s

        answer = []
        line, width = [], 0
        for w in words:
            if width + len(w) + len(line) <= maxWidth:
                line.append(w)
                width += len(w)
            else:
                answer.append(justify(line, width, maxWidth))
                line, width = [w], len(w)
        answer.append(' '.join(line) + (maxWidth - width - len(line) + 1) * ' ')
        return answer