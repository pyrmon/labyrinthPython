/**
 * Author: MasterMax13124
 * Last updated: recently?
 * To-Do: Implement handWallSolver and later Pledge algorithm as static methods
 */

class labyrinthsolver{
	public static void main(String[] args){
		labyrinth lab = new labyrinth("labyrinth.map");

		//Der Block hier drunter checkt eigentlich nur die traveler position und so
		// System.out.println(lab.getTravelerPos()[0]);
		// System.out.println(lab.getTravelerPos()[1]);
		// System.out.println(lab.getMap()[32][15]);

		System.out.println(lab.getTravelerSurroundings());
		lab.changeDirection(1);
		System.out.println(lab.getTravelerSurroundings());

		// lab.moveTraveler();
		// System.out.println(lab.getTravelerPos()[0]);
		// System.out.println(lab.getTravelerPos()[1]);
		// lab.changeDirection(1);
		// lab.moveTraveler();
		// System.out.println(lab.getTravelerPos()[0]);
		// System.out.println(lab.getTravelerPos()[1]);

		// lab.moveTraveler();
		// lab.changeDirection(1);
		// lab.moveTraveler();
		// lab.changeDirection(-1);
		// lab.moveTraveler();
		// lab.changeDirection(1);
		// lab.moveTraveler();
		// int a = lab.getTravelerPos()[0];
		// int b = lab.getTravelerPos()[1];
		// System.out.println(a);
		// System.out.println(b);
		// System.out.println(lab.getMap()[a][b]);
		
	}

	public static void handWallSolver() {

	}
}
