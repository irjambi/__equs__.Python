import sys
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style="darkgrid")
# plt.style.use('seaborn-darkgrid')

# num = int(sys.argv[1])

steppy = 1e3
steps = []
n_min = int(sys.argv[1])
n_max = int(sys.argv[2])+1

for num in range(n_min,n_max):
	s = 0
	while s < steppy:
		if num <= 1:
			# exit()
			break

		elif num%2 == 0:
			# print(int(num/2))
			num = int(num/2)

		else:
			# print(num*3+1)
			num = int(num*3+1)

		s = s+1

	steps.append(s)


fig = plt.figure(figsize=(16,9), dpi= 80)
ax1 = fig.add_subplot(111)
# sns.set_style("darkgrid", {"axes.facecolor": ".1"})
plt.plot(range(n_min,n_max),steps, linewidth = 2)

# Set plotting attributes   
plt.xlabel('Number', fontsize=24)
plt.xlim([n_min,n_max])

plt.ylabel('Steps' , fontsize=24)
# plt.ylim([0.1,1])

plt.tick_params(labelright=False, which='both', length=6, width=2, labelsize=22)
# ax1.yaxis.set_ticks_position('both')
plt.grid()
# plt.legend(loc=3,fontsize=22);

# sns.set()
plt.show(block=False)

# sns.relplot(x="Number", y="Steps", data=steps);
