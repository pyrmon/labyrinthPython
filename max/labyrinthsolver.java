class labyrinthsolver{
	public static void main(String[] args){
		labyrinth lab = new labyrinth("labyrinth.txt");
		//lab.printLabyrinth();
		// System.out.println(lab.getLabyrinthAsString());
		// System.out.println(lab.getTravelerPos()[0]);
		// System.out.println(lab.getTravelerPos()[1]);
		System.out.println(lab.getMap()[32][15]);
		lab.changeDirection(0);
	}

	public static void handWallSolver() {

	}
}
