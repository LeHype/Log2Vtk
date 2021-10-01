c =======================================================================
      
       SUBROUTINE UEL (RHS, AMATRX, SVARS, ENERGY, NDOFEL, NRHS, NSVARS,
     & PROPS, NPROPS, COORDS, MCRD, NNODE, U, DU, V, A, JTYPE, TIME,
     & DTIME, KSTEP, KINC, JELEM, PARAMS, NDLOAD, JDLTYP, ADLMAG,
     & PREDEF, NPREDF, LFLAGS, MLVARX, DDLMAG, MDLOAD, PNEWDT, JPROPS,
     & NJPRO, PERIOD)
      
       INCLUDE 'ABA_PARAM.INC'

       DIMENSION RHS(NDOFEL), AMATRX(NDOFEL,NDOFEL), PROPS(*),
     & SVARS(*), ENERGY(8), COORDS(MCRD, NNODE), U(NDOFEL),
     & DU(NDOFEL), V(12), A(12), TIME(2), PARAMS(*),
     & JDLTYP(MDLOAD,*), ADLMAG(MDLOAD,*), DDLMAG(MDLOAD,*),
     & PREDEF(2, NPREDF, NNODE), LFLAGS(*), JPROPS(*)
      
      RHS = 0.0
      AMATRX = 0.0
      call ParaviewPreProcessing('U',3,U,TIME,JELEM,NNODE)
      call ParaviewPreProcessing('S',1,U,TIME,JELEM,NNODE)
      call ParaviewPreProcessing('T',1,U,TIME,JELEM,NNODE)
      Write(6,*) 'MCRD = ', MCRD
      End 
      SUBROUTINE ParaviewPreProcessing(ID,VPN,Var,Zeit,ELEM,NPE)
        implicit none
        character (len=1)             :: ID
        integer                       :: VPN,NPE,i,j,ELEM
        Real(8), DIMENSION(4*VPN)     :: Var
        Real(8), DIMENSION(2)         :: ZEIT

        WRITE(6,*) 'Time =',',', ZEIT(1),',','ELEM',',',ELEM
        WRITE(6,*) 'UNIQUE ID = ', ',' , ID
        Do i = 1,VPN
        DO j = 1,NPE
          WRITE(6,*) Var(i+j)
        END DO 
        END DO 
        End SUBROUTINE
