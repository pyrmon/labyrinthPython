import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Arrays;
import java.util.*;

class labyrinth{
	private String inputFile;
	private char[][] map;

	public labyrinth(String filename){
		List<String> templist = new ArrayList<String>();

		try {
			File myObj = new File(filename);
    	Scanner myReader = new Scanner(myObj);
			
    	while (myReader.hasNextLine()) {
				//String data = myReader.nextLine();
				templist.add(myReader.nextLine());
			}
			myReader.close();
		}
		catch(FileNotFoundException e){
			System.out.println("An error occured!");
		}

		int xsize = templist.get(0).length();
		map = new char[xsize][templist.size()];

		for(int i = 0; i < templist.size(); i++) {
			for(int j = 0; j < xsize; j++){
				map[i][j] = templist.get(i).charAt(j);
			}
		}
	}

	public void printLabyrinth(){
		for(int i = 0; i < map.length; i++){
			for(int j = 0; j < map[0].length; j++){
				System.out.println(map[i][j]);
			}
		}
	}
}
