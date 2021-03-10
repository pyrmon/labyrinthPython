/**
 * Author: MasterMax13124
 * Last updated: recently?
 * To-Do: Check for bugs in handWallSolver
 */

class labyrinthsolver{
	public static void main(String[] args){
		handWallSolver("labyrinth.map").printMap();
	}

	//implements the left hand algorithm
	public static labyrinth handWallSolver(String filename) {
		labyrinth lab = new labyrinth(filename);
		lab.changeDirection(1); //for demo purposes only, not part of the final algorithm

		while(lab.getTravelerSurroundings()[0] != 'X') {
			if (lab.getTravelerSurroundings()[2] != '#' && lab.getTravelerSurroundings()[1] == '#') { //move forwards if the space is empty and there is wall to the left
				lab.moveTraveler();
				continue;
			}

			if (lab.getTravelerSurroundings()[2] == '#') { //handles turning with various walls in the way
				if (lab.getTravelerSurroundings()[1] != '#') {
					lab.changeDirection(-1);
					lab.moveTraveler();
				}
				else if (lab.getTravelerSurroundings()[3] != '#') {
					lab.changeDirection(1);
					lab.moveTraveler();
				}
				else {
					lab.changeDirection(2);
					lab.moveTraveler();
				}
				continue;
			}

			if (lab.getTravelerSurroundings()[2] != '#' && lab.getTravelerSurroundings()[1] != '#') { //turn to the left if theres no wall to follow
				lab.changeDirection(-1);
				lab.moveTraveler();
				continue;
			}

		} //end of while loop

		lab.moveTraveler(); //move the traveler one last time into the goal, so the last arrow gets drawn
		return lab;
	}
}
