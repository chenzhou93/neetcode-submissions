class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m_char1 = {}
        m_char2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in m_char1:
                m_char1[char] += 1
            else:
                m_char1[char] = 0
        
        for char in t:
            if char in m_char2:
                m_char2[char] += 1
            else:
                m_char2[char] = 0
        
        long_m = m_char1 if len(m_char1) > len(m_char2) else m_char2

        for key, value in m_char1.items():
            if key in m_char2:
                if m_char2[key] != value:
                    return False
            else:
                return False
        
        return True
        
        