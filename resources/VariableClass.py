import numpy as np
class Variable():
      def __init__(self,UniqueId,NumberNodes,NumberComponents,TimeIncrements):
            self.UniqueId= UniqueId
            self.NumberNodes= NumberNodes
            self.NumberComponents= NumberComponents
            self.TimeIncrements = TimeIncrements

            self.Data= np.zeros((len(self.TimeIncrements),self.NumberNodes,self.NumberComponents))
            