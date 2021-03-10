import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Arrays;
import java.util.*;

/**
 * Author: MasterMax13124
 * Last updated: recently?
 * To-Do: Refine movement for traveler, possibly add/edit some methods
 */

class labyrinth {
	private String inputFile; //contains the entire inputfile as a string, currently unused
	private char[][] map; //2d array of the maze, first index is x, second is y
	private int mapxsize;
	private int mapysize;

	//Traveler specific variables
	private int travelerX;
	private int travelerY;
	private int travelerD; //direction, 0 is up, 1 is right etc, can go higher than 3 for pledge algorithm

	/**
	 * Constructor for class labyrinth
	 * @param filename Pass filename of map in working directory as string
	 */
	public labyrinth(String filename) { // Constructor immediately splits the file into a char array for later
										// operations
		List<String> templist = new ArrayList<String>();

		try {
			File myObj = new File(filename);
			Scanner myReader = new Scanner(myObj);

			while (myReader.hasNextLine()) {
				String data = myReader.nextLine();
				templist.add(data);
				inputFile += data + "\n";

				// Automatically save starting point position
				if (data.contains("S")) {
					travelerY = templist.size() - 1;
					travelerX = data.indexOf("S");
				}
			}
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("An error occured!");
		}

		int xsize = templist.get(0).length();
		map = new char[xsize][templist.size()];
		this.mapxsize = xsize;
		this.mapysize = templist.size();

		for (int i = 0; i < templist.size(); i++) {
			for (int j = 0; j < xsize; j++) {
				map[j][i] = templist.get(i).charAt(j);
			}
		}
	}

	/**
	 * Positive input will change clockwise, negative counterclockwise.
	 * Passing 0 will do nothing.
	 */
	public void changeDirection(int directionChange) {
		this.travelerD += directionChange;
	}

	/**
	 * Moves the traveler one position.
	 * To change direction, call changeDirection and pass an int.
	 */
	public void moveTraveler() {
		int[] newcoords = calculatePosition(this.travelerX, this.travelerY, this.travelerD);
		this.travelerX = newcoords[0];
		this.travelerY = newcoords[1];
	}

	/**
	 * I seperated this from moveTraveler() so I can potentially reuse it somewhere else later.
	 */
	private int[] calculatePosition(int xcoord, int ycoord, int direction) {
		int xcoordn = xcoord;
		int ycoordn = ycoord;

		switch(direction % 4) {
			case 0:
				ycoordn = ycoord > 0 ? ycoord -1 : ycoord;
				break;
			case 1:
				xcoordn = xcoord > 0 ? xcoord -1 : xcoord;
				break;
			case 2:
				ycoordn = ycoord < this.mapysize ? ycoord -1 : ycoord;
				break;
			case 3:
				xcoordn = xcoord < this.mapxsize ? xcoord -1 : xcoord;
				break;
			default:
				System.out.println("Something is wrong with the position calculation lmao");
				break;
		}

		return new int[]{xcoordn, ycoordn};
	}

	/**
	 * Returns the current map as char array. That's about it.
	 */
	public char[][] getMap() {
		return map;
	}

	/**
	 * Returns the travelers current position and direction as 3 ints.
	 * @return X coord, Y coord, direction in that order.
	 */
	public int[] getTravelerPos() {
		int[] pos = {this.travelerX, this.travelerY, this.travelerD};
		return pos;
	}
}
