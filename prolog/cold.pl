%B: book
%A: age
%I: interest
%L: language
%Need to extend for more examples

suggest(B):- 
write('Do you have chiils? '),
read(A),
write('Do you have Sore_throat? '),
read(I),
write('Do you have Cough? '),
read(L), 
write('Do you have headache? '),
read(H),
write('Do you have fatigue? '),
read(F),
book(B,A,I,L,H,F).

book('cold', A,I,L,H,F):- A = yes, I= yes, L=no,H=no,F=yes,!.
book('cold', A,I,L,H,F):- A = yes, I=no, L=yes,H=yes,F=no!.

book('fever', A,I,L,H,F):-A = no, I=yes, L=no,H=yes,F=yes,!.
book('fever', A,I,L,H,F):- A = yes, I=no, L=no,H=yes,F=yes,!.

