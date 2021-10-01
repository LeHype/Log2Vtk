1

   Abaqus 3DEXPERIENCE R2017x                                  Date 01-Okt-2021   Time 10:21:58
   For use by UNIVERSITAET DES SAARLANDES under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

          FIXED TIME INCREMENTS
          TIME INCREMENT IS                                    0.100    
          TIME PERIOD IS                                        1.00    

     LINEAR EQUATION SOLVER TYPE         DIRECT SPARSE

 CONVERGENCE TOLERANCE PARAMETERS FOR FORCE    
     CRITERION FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR DISP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE FORCE                               1.000E-02
     AVERAGE FORCE     IS TIME AVERAGE FORCE    
     ALTERNATE CRIT. FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO FORCE     RELATIVE TO TIME AVRG. FORCE         1.000E-05
     CRITERION FOR RESIDUAL FORCE     WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR DISP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL FORCE     FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO FORCE     REL. TO TIME AVRG. MAX. FORCE        1.000E-05
     CRITERION FOR ZERO DISP.    RELATIVE TO CHARACTERISTIC LENGTH     1.000E-08

     VOLUMETRIC STRAIN COMPATIBILITY TOLERANCE FOR HYBRID SOLIDS       1.000E-05
     AXIAL STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS             1.000E-05
     TRANS. SHEAR STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS      1.000E-05
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P>P0          5.000E-03
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P=0.0         0.100    
     CONTACT FORCE ERROR TOLERANCE FOR CONVERT SDI=YES                 1.00    
     DISPLACEMENT COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS           1.000E-05
     ROTATION COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS               1.000E-05

 EQUILIBRIUM WILL BE CHECKED FOR SEVERE DISCONTINUITY ITERATIONS

 ITERATION CONTROL PARAMETERS:
     FIRST EQUILIBRIUM ITERATION FOR CONSECUTIVE DIVERGENCE CHECK              4
     EQUILIBRIUM ITERATION AFTER WHICH ALTERNATE RESIDUAL IS USED              9
     MAXIMUM EQUILIBRIUM ITERATIONS ALLOWED                                   16
     MAXIMUM ITERATIONS FOR SEVERE DISCONTINUITIES                            12
     GLOBAL STABILIZATION CONTROL IS NOT USED

          PRINT OF INCREMENT NUMBER, TIME, ETC., EVERY    1  INCREMENTS

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                     100

     LINEAR EXTRAPOLATION WILL BE USED

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    

 ***WARNING: THERE ARE 3 UNCONNECTED REGIONS IN THE MODEL.

  NUMBER OF EQUATIONS =        34     NUMBER OF FLOATING PT. OPERATIONS =  1.68E+03

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.31 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.32 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.37 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.

 ***WARNING: SOLVER PROBLEM.  ZERO PIVOT WHEN PROCESSING NODE 38 INSTANCE 
             PART-1-1 D.O.F. 2
  Typically a zero pivot is associated with an overconstraint in the model. 
 However, Abaqus was not able to identify any chains of constraints that might 
 lead to an overconstraint at this node. This suggests that the model might be 
 in fact insufficiently constrained in this particular degree of freedom. 
 Please check the constraints used in this model. 


 ***WARNING: Solver problem. Zero pivot when processing D.O.F. 2 of 1 nodes. 
             The nodes have been identified in node set 
             WarnNodeSolvProbZeroPiv_2_1_1_1_1.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.475E+07   TIME AVG. FORCE       1.475E+07
 LARGEST RESIDUAL FORCE            -9.000E+08   AT NODE         31   DOF  2
   INSTANCE: PART-1-1                                                                        
 ALL DISP.    INCREMENTS ARE ZERO
 ALL CORRECTION TO DISP.    ARE ZERO
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

  NUMBER OF EQUATIONS =        34     NUMBER OF FLOATING PT. OPERATIONS =  1.68E+03

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =  1.00000E-02
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.31 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.32 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.37 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.

 ***WARNING: SOLVER PROBLEM.  ZERO PIVOT WHEN PROCESSING NODE 38 INSTANCE 
             PART-1-1 D.O.F. 2
  Typically a zero pivot is associated with an overconstraint in the model. 
 However, Abaqus was not able to identify any chains of constraints that might 
 lead to an overconstraint at this node. This suggests that the model might be 
 in fact insufficiently constrained in this particular degree of freedom. 
 Please check the constraints used in this model. 


 ***WARNING: Solver problem. Zero pivot when processing D.O.F. 2 of 1 nodes. 
             The nodes have been identified in node set 
             WarnNodeSolvProbZeroPiv_2_1_1_2_1.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      1.475E+07   TIME AVG. FORCE       1.475E+07
 LARGEST RESIDUAL FORCE            -9.000E+08   AT NODE         31   DOF  2
   INSTANCE: PART-1-1                                                                        
 ALL DISP.    INCREMENTS ARE ZERO
 ALL CORRECTION TO DISP.    ARE ZERO
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

  NUMBER OF EQUATIONS =        34     NUMBER OF FLOATING PT. OPERATIONS =  1.68E+03

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.31 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.32 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.37 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.

 ***WARNING: SOLVER PROBLEM.  ZERO PIVOT WHEN PROCESSING NODE 38 INSTANCE 
             PART-1-1 D.O.F. 2
  Typically a zero pivot is associated with an overconstraint in the model. 
 However, Abaqus was not able to identify any chains of constraints that might 
 lead to an overconstraint at this node. This suggests that the model might be 
 in fact insufficiently constrained in this particular degree of freedom. 
 Please check the constraints used in this model. 


 ***WARNING: Solver problem. Zero pivot when processing D.O.F. 2 of 1 nodes. 
             The nodes have been identified in node set 
             WarnNodeSolvProbZeroPiv_2_1_1_3_1.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      1.475E+07   TIME AVG. FORCE       1.475E+07
 LARGEST RESIDUAL FORCE            -9.000E+08   AT NODE         31   DOF  2
   INSTANCE: PART-1-1                                                                        
 ALL DISP.    INCREMENTS ARE ZERO
 ALL CORRECTION TO DISP.    ARE ZERO
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

  NUMBER OF EQUATIONS =        34     NUMBER OF FLOATING PT. OPERATIONS =  1.68E+03

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  1.00000E-02
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  1.00000E-02
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.31 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.32 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PART-1-1.37 D.O.F. 2. THIS NODE HAS NO STIFFNESS IN THE SPECIFIED 
             DIRECTION AND IS NOT COUPLED WITH THE REST OF THE MODEL.

 ***WARNING: SOLVER PROBLEM.  ZERO PIVOT WHEN PROCESSING NODE 38 INSTANCE 
             PART-1-1 D.O.F. 2
  Typically a zero pivot is associated with an overconstraint in the model. 
 However, Abaqus was not able to identify any chains of constraints that might 
 lead to an overconstraint at this node. This suggests that the model might be 
 in fact insufficiently constrained in this particular degree of freedom. 
 Please check the constraints used in this model. 


 ***WARNING: Solver problem. Zero pivot when processing D.O.F. 2 of 1 nodes. 
             The nodes have been identified in node set 
             WarnNodeSolvProbZeroPiv_2_1_1_4_1.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     4


 AVERAGE FORCE                      1.475E+07   TIME AVG. FORCE       1.475E+07
 LARGEST RESIDUAL FORCE            -9.000E+08   AT NODE         31   DOF  2
   INSTANCE: PART-1-1                                                                        
 ALL DISP.    INCREMENTS ARE ZERO
 ALL CORRECTION TO DISP.    ARE ZERO
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.
 

 ***NOTE: THE SOLUTION APPEARS TO BE DIVERGING. CONVERGENCE IS JUDGED UNLIKELY.
 

 ***ERROR: FIXED TIME INCREMENT IS TOO LARGE



     ANALYSIS SUMMARY:
     TOTAL OF          1  INCREMENTS
                       1  CUTBACKS IN AUTOMATIC INCREMENTATION
                       4  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                       4  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                       4  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       1  WARNING MESSAGES DURING USER INPUT PROCESSING
                      21  WARNING MESSAGES DURING ANALYSIS
                      16  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       1  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =  8.00000E-02
       SYSTEM TIME (SEC)    =  2.00000E-02
       TOTAL CPU TIME (SEC) =  0.10000    
       WALLCLOCK TIME (SEC) =          1
