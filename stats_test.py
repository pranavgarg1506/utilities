import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

from scipy import stats

class Assumptions:
    
    def summary():
        pass
    
    def plot_graph(self,data):
        sns.displot(data, kde = True, color ='red', bins = 30)
        plt.tight_layout()
        plt.show()
        
    def basic_profiling(self):
        a1 = self.grp1['data']
        b1 = self.grp2['data']
        
        print(f"group 1 contains {len(a1)} elements in it with a mean of {round(np.mean(a1),2)}")
        print(f"group 2 contains {len(b1)} elements in it with a mean of {round(np.mean(b1),2)}")
        
        print("Plotting Grpahs for all distributions.......................")
        self.plot_graph(self.grp1['data'])
        self.plot_graph(self.grp2['data'])
        
        
    def ac_normality_test(self):
        
        print("performing Normality Test..........................")
        self.grp1['normality_f_stat'],self.grp1['normality_pvalue']  = stats.shapiro(self.grp1['data'])
        print(f"for group 1 fstat value is {self.grp1['normality_f_stat']} and pvalue is {self.grp1['normality_pvalue']}")
        self.grp2['normality_f_stat'],self.grp2['normality_pvalue']  = stats.shapiro(self.grp2['data'])
        print(f"for group 2 fstat value is {self.grp2['normality_f_stat']} and pvalue is {self.grp2['normality_pvalue']}")
        
    def ac_homogenity_test(self):
        print("performing Homogenity Test.........................")
        f_stat, self.general['homogenity_pvalue'] = stats.levene(self.grp1['data'], self.grp2['data'])
        print(f"fstat value is {f_stat} and pvalue is {self.general['homogenity_pvalue']}")
    
    
    
class ParametricTests(Assumptions):
    
    def __init__(self) -> None:
        super().__init__()
    
    def independent_t_test(self,*args):
        """
        Checking 2 independent samples on the basis of independent t test
        """
        pass
        
        
        
class CheckStats(ParametricTests):
    
    def __init__(self,*args) -> None:
        
        print("Calling stats Library to check the statistical significance of the groups.........")
        print(f"You have passed {len(args)} arguments for the analysis................")
        
        if len(args) == 2:
            self.grp1 = {}
            self.grp2 = {}
            self.general = {}
            self.grp1['data'] = args[0]
            self.grp2['data'] = args[1]
            Assumptions.basic_profiling(self)
            
            t_test_type = input("\nWhich Test do you want to perform?\nSelect 'A' for independent t test or 'B' for paired t test\n")
            
            if t_test_type.lower() == 'a':
                print("\nperforming Independent t test.................\nchecking assumptions of t test..................")
                Assumptions.ac_normality_test(self)
                Assumptions.ac_homogenity_test(self)
                
                cond1 = self.grp1['normality_pvalue'] > 0.05
                cond2 = self.grp2['normality_pvalue'] > 0.05
                cond3 = self.general['homogenity_pvalue'] > 0.05

                if cond1 & cond2 & cond3:
                    print("Suggesting independent t test.....................")
                    f_stat,pvalue = stats.ttest_ind(self.grp1['data'],self.grp2['data'])
                elif cond1 & cond2 & ~cond3:
                    print("Suggesting welch test.....................")
                    f_stat,pvalue = stats.ttest_ind(self.grp1['data'],self.grp2['data'],equal_var=False)
                else:
                    print("Suggesting Mann Whitney T test.....................")
                    f_stat,pvalue = stats.mannwhitneyu(self.grp1['data'],self.grp2['data'])

                print(f"U-statistic: {f_stat}")
                print(f"pvalue is {pvalue}")
        
        
        super().__init__()
        