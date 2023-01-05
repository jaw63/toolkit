"""
From https://www.analyticsvidhya.com/blog/2021/07/cyberpunk-themed-charts-advanced-data-visualization-in-python/

Important:
    First run this command in terminal or cmd
    pip install mplcyberpunk
    
"""
import matplotlib.pyplot as plt
import mplcyberpunk
plt.style.use('cyberpunk')
plt.figure(figsize = (20,8))
plt.plot([1,4,6,7,4,1], marker = 'o')
plt.plot([5,3,5,8,9,2], marker = 'o')
plt.plot([3,5,8,3,4,9], marker = 'o')
plt.xticks(size = 16)
plt.yticks(size = 16)
mplcyberpunk.make_lines_glow()
plt.show()