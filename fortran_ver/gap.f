C PROGRAM TO CALCULATE THE PAIRING GAP IN MASSES
      IMPLICIT REAL * 8 (A-H, O-Z)			          
      DIMENSION E(8)						          
C E(1)=M(A-5)							          
C E(2)=M(A-3)							          
C E(3)=M(A-2)							       
C E(4)=M(A-1)							       
C E(5)=M(A)								
C E(6)=M(A+1)							        
C E(7)=M(A+3)
C E(8)=M(A+5)
      N=0
      READ(5,99)NCAS
 1000 READ (5,101) NOYAU, PART
      WRITE (6,201) NOYAU,PART
      N=N+1
      DO 1 I=1,8
        READ (5,100) E(I)
        WRITE(6,200) E(I)
 1    CONTINUE
      D11=E(5)-0.5*E(4)-0.5*E(6)
      WRITE(6,211) D11
      IF (E(7).EQ.0.D0) GO TO 5
      D12=E(5)-0.375*E(4)-0.75*E(6)+0.125*E(7)
      WRITE(6,212) D12
      IF (E(2).EQ.0.D0) GO TO 2
 5    D13=E(5)+0.125*E(2)-0.75*E(4)-0.375*E(6)
      WRITE(6,213) D13
      IF (E(1).EQ.0.D0) GO TO 3
      D14=E(5)-0.0625*E(1)+0.3125*E(2)-0.9375*E(4)-0.3125*E(6)
      WRITE(6,214) D14
 3    IF (E(7).EQ.0.D0) GO TO 4
      D15=E(5)+0.0625*E(2)-0.5625*E(4)-0.5625*E(6)+0.0625*E(7)
      WRITE(6,215) D15
 2    IF (E(8).EQ.0.D0) GO TO 4
      D16=e(5)-.3125*e(4)-.9375*e(6)+.3125*e(7)-0.0625*e(8)
      WRITE(6,216) D16
 4    IF (E(3).EQ.0.D00) GO TO 6
      DNP=0.25*E(3)-0.75*E(4)+0.75*E(5)-0.25*E(6)
      WRITE(6,217) DNP
 6    IF (N.LT.NCAS) GO TO 1000
 99   FORMAT(I2)
 100  FORMAT(F9.3)
 101  FORMAT(2A4)
 200  FORMAT(1H0,3X,F9.3)
 201  FORMAT(1H0,3X,2A4)
 211  FORMAT(1H0,5X,4HD11=,D13.6)
 212  FORMAT(1H0,5X,4HD12=,D13.6)
 213  FORMAT(1H0,5X,4HD13=,D13.6)
 214  FORMAT(1H0,5X,4HD14=,D13.6)
 215  FORMAT(1H0,5X,4HD15=,D13.6)
 216  FORMAT(1H0,5X,4HD16=,D13.6)
 217  FORMAT(1H0,5X,4HDNP=,D13.6)
      END
