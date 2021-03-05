package io.fyp.fypapi.data;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.time.Duration;
import java.time.Instant;

import org.springframework.stereotype.Service;


@Service
public class DataService {

	private String csvFile = "F:\\ACADEMIC\\Semester 7\\CO 421 CO 425 Final Year Project\\Project\\fyp-dataset-api\\API-Test\\src\\main\\java\\io\\fyp\\fypapi\\data\\dataset.csv";
	private String line = "";
	private String cvsSplitBy = ",";
    
	private ArrayList<Double> time = new ArrayList<Double>();
	private ArrayList<Double> vehicle_speed = new ArrayList<Double>();
	private ArrayList<Double> shift_number = new ArrayList<Double>();
	private ArrayList<Double> engine_load = new ArrayList<Double>();
	private ArrayList<Double> total_acceleration = new ArrayList<Double>();
	private ArrayList<Double> engine_rpm = new ArrayList<Double>();
	private ArrayList<Double> pitch = new ArrayList<Double>();
	private ArrayList<Double> lateral_acceleration = new ArrayList<Double>();
	private ArrayList<Double> passenger_count = new ArrayList<Double>();
	private ArrayList<Double> cars_load = new ArrayList<Double>();
	private ArrayList<Double> air_condition_status = new ArrayList<Double>();
	private ArrayList<Double> window_opening = new ArrayList<Double>();
	private ArrayList<Double> radio_volume = new ArrayList<Double>();
	private ArrayList<Double> rain_intensity = new ArrayList<Double>();
	private ArrayList<Double> visibility = new ArrayList<Double>();
	private ArrayList<Double> drivers_wellbeing = new ArrayList<Double>();
	private ArrayList<Double> driver_rush = new ArrayList<Double>();

	private int [] number_of_requests = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    
	private Instant start;
	private Instant end;
	
	{
	    try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
	
	        while ((line = br.readLine()) != null) {
	
	            // use comma as separator
	        	
	            String[] data = line.split(cvsSplitBy);
	            
//	            System.out.println(data[0]);
	            
	            time.add(Double.parseDouble(data[0]));
	            vehicle_speed.add(Double.parseDouble(data[1]));
	            shift_number.add(Double.parseDouble(data[2]));
	            engine_load.add(Double.parseDouble(data[3]));
	            total_acceleration.add(Double.parseDouble(data[4]));
	            engine_rpm.add(Double.parseDouble(data[5]));
	            pitch.add(Double.parseDouble(data[6]));
	            lateral_acceleration.add(Double.parseDouble(data[7]));
	            passenger_count.add(Double.parseDouble(data[8]));
	            cars_load.add(Double.parseDouble(data[9]));
	            air_condition_status.add(Double.parseDouble(data[10]));
	            window_opening.add(Double.parseDouble(data[11]));
	            radio_volume.add(Double.parseDouble(data[12]));
	            rain_intensity.add(Double.parseDouble(data[13]));
	            visibility.add(Double.parseDouble(data[14]));
	            drivers_wellbeing.add(Double.parseDouble(data[15]));
	            driver_rush.add(Double.parseDouble(data[16]));
	            	
	        }
	        
	        start = Instant.now();
	
	    } catch (IOException e) {
	        e.printStackTrace();
	    }
    }
	
	public int getLength(Duration timeElapsed, int start_i) {
		for (int i = start_i; i < time.size(); i++) {
			if(time.get(i) > timeElapsed.toSeconds()) {
				return i;
			}
		}
		
		return -1;
	}

	
    public ArrayList<Double> getData(String id) {
    	int length_to_send, begining_length;
    	Duration timeElapsed;
//		System.out.println(count);
		switch(id) {
			case "time":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[0]);
				begining_length = number_of_requests[0];
				
				number_of_requests[0] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(time.subList(begining_length, length_to_send));
			
			case "vehicleSpeed":
				
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[1]);
				begining_length = number_of_requests[1];
				
				number_of_requests[1] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);

				return new ArrayList<Double>(vehicle_speed.subList(begining_length, length_to_send));
			
			case "shiftNumber":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[2]);
				begining_length = number_of_requests[2];
				
				number_of_requests[2] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(shift_number.subList(begining_length, length_to_send));
			
			case "engineLoad":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[3]);
				begining_length = number_of_requests[3];
				
				number_of_requests[3] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(engine_load.subList(begining_length, length_to_send));
			
			case "totalAcceleration":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[4]);
				begining_length = number_of_requests[4];
				
				number_of_requests[4] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(total_acceleration.subList(begining_length, length_to_send));
			
			case "engineRPM":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[5]);
				begining_length = number_of_requests[5];
				
				number_of_requests[5] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(engine_rpm.subList(begining_length, length_to_send));
			
			case "pitch":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[6]);
				begining_length = number_of_requests[6];
				
				number_of_requests[6] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(pitch.subList(begining_length, length_to_send));
			
			case "lateralAcceleration":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[7]);
				begining_length = number_of_requests[7];
				
				number_of_requests[7] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(lateral_acceleration.subList(begining_length, length_to_send));
			
			case "passengerCount":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[8]);
				begining_length = number_of_requests[8];
				
				number_of_requests[8] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(passenger_count.subList(begining_length, length_to_send));
			
			case "carLoad":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[9]);
				begining_length = number_of_requests[9];
				
				number_of_requests[9] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(cars_load.subList(begining_length, length_to_send));
			
			case "airConditionStatus":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[10]);
				begining_length = number_of_requests[10];
				
				number_of_requests[10] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(air_condition_status.subList(begining_length, length_to_send));
			
			case "windowOpening":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[11]);
				begining_length = number_of_requests[11];
				
				number_of_requests[11] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(window_opening.subList(begining_length, length_to_send));
			
			case "radioVolume":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[12]);
				begining_length = number_of_requests[12];
				
				number_of_requests[12] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(radio_volume.subList(begining_length, length_to_send));
			
			case "rainIntensity":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[13]);
				begining_length = number_of_requests[13];
				
				number_of_requests[13] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(rain_intensity.subList(begining_length, length_to_send));
			
			case "visibility":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[14]);
				begining_length = number_of_requests[14];
				
				number_of_requests[14] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(visibility.subList(begining_length, length_to_send));
			
			case "DriverWellBeing":
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[15]);
				begining_length = number_of_requests[15];
				
				number_of_requests[15] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(drivers_wellbeing.subList(begining_length, length_to_send));
			
			default:
				end = Instant.now();
				timeElapsed = Duration.between(start, end);
				
				length_to_send = getLength(timeElapsed, number_of_requests[16]);
				begining_length = number_of_requests[16];
				
				number_of_requests[16] = length_to_send;
				
//				System.out.println("Time taken: "+ timeElapsed.toSeconds() +" seconds");
//				System.out.println("length: "+ length_to_send);
				
				return new ArrayList<Double>(driver_rush.subList(begining_length, length_to_send));
		}
	}
}

