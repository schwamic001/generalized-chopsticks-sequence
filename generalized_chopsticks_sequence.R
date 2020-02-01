# Generalized Chopsticks Sequence
# Alexander Robinson & Michael Schwalen
# Code assistance from Angela Lin
# April 7, 2018

# This code simulates the Generalized Chopsticks Sequence (A302403).

# Load library
library(dplyr)

# Create function
chopsticks <- function(n) {
  
  # Initialize empty variables
  num_turns_p1_wins=c()  
  num_turns_p2_wins=c()
  num_p1_wins=0
  num_p2_wins=0
  
  # Run loop to determine round winners
  for(j in 1:(n-1)){
    p1=j
    p2=j
    for(i in 1:(n-1)){
      p2=p1+p2
      p1=p2+p1
      i=i+1
      if(p2%%n==0){
        num_p1_wins=num_p1_wins+1
        num_turns_p1_wins=c(num_turns_p1_wins,i)
        break
      }
      if(p1%%n==0){
        num_p2_wins=num_p2_wins+1
        num_turns_p2_wins=c(num_turns_p2_wins,i)
        break
      }
      p2=p2%%n
      p1=p1%%n
    }
  }
  
  # Determine final winner
  winner <- ifelse(num_p2_wins == n-1,"P2",ifelse(num_p1_wins == n-1,"P1","Neither"))
  return(winner)
}

# Simulate n 1:1000
simulation <- data.frame(n = 1:1000)
simulation$winner <- lapply(simulation$n,chopsticks)

# Create sequence
sequence <- filter(simulation,winner != "Neither")
sequence <- sequence$n
sequence

# Create list output
paste0(paste0(as.character(sequence),", "), collapse = "")
