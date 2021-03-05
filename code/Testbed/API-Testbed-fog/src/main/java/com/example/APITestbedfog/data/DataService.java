package com.example.APITestbedfog.data;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.time.Duration;
import java.time.Instant;

import org.springframework.stereotype.Service;


@Service
public class DataService {

	private String csvFile = "F:\\ACADEMIC\\Semester 7\\CO 421 CO 425 Final Year Project\\Project\\fyp-dataset-api\\API-Testbed\\src\\main\\java\\io\\fyp\\fypapi\\ssdata.csv";
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

	private int [] number_of_requests = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
    
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
	
//	public int getLength(Duration timeElapsed) {
//		for (int i = 0; i < time.size(); i++) {
//			if(time.get(i) > timeElapsed.toSeconds()) {
//				return i - 1;
//			}
//		}
//		
//		return -1;
//	}

	
    public ArrayList<Double> getData(String id) {
    	int length_to_send;
//		System.out.println(count);
		switch(id) {
			case "time":
				number_of_requests[0] += 1;
				return new ArrayList<Double>(time.subList(number_of_requests[0] * 5, (number_of_requests[0] * 5) + 5));
			
			case "vehicleSpeed":
				number_of_requests[1] += 1;
				
//				end = Instant.now();
//				Duration timeElapsed = Duration.between(start, end);
//				length_to_send = getLength(timeElapsed);
//				start = Instant.now();
				
//				System.out.println("Time taken: "+ timeElapsed.toMillis() +" milliseconds");

				return new ArrayList<Double>(vehicle_speed.subList(number_of_requests[1] * 5, (number_of_requests[1] * 5) + 5));
			
			case "shiftNumber":
				number_of_requests[2] += 1;
				return new ArrayList<Double>(shift_number.subList(number_of_requests[2] * 5, (number_of_requests[2] * 5) + 5));
			
			case "engineLoad":
				number_of_requests[3] += 1;
				return new ArrayList<Double>(engine_load.subList(number_of_requests[3] * 5, (number_of_requests[3] * 5) + 5));
			
			case "totalAcceleration":
				number_of_requests[4] += 1;
				return new ArrayList<Double>(total_acceleration.subList(number_of_requests[4] * 5, (number_of_requests[4] * 5) + 5));
			
			case "engineRPM":
				number_of_requests[5] += 1;
				return new ArrayList<Double>(engine_rpm.subList(number_of_requests[5] * 5, (number_of_requests[5] * 5) + 5));
			
			case "pitch":
				number_of_requests[6] += 1;
				return new ArrayList<Double>(pitch.subList(number_of_requests[6] * 5, (number_of_requests[6] * 5) + 5));
			
			case "lateralAcceleration":
				number_of_requests[7] += 1;
				return new ArrayList<Double>(lateral_acceleration.subList(number_of_requests[7] * 5, (number_of_requests[7] * 5) + 5));
			
			case "passengerCount":
				number_of_requests[8] += 1;
				return new ArrayList<Double>(passenger_count.subList(number_of_requests[8] * 5, (number_of_requests[8] * 5) + 5));
			
			case "carLoad":
				number_of_requests[9] += 1;
				return new ArrayList<Double>(cars_load.subList(number_of_requests[9] * 5, (number_of_requests[9] * 5) + 5));
			
			case "airConditionStatus":
				number_of_requests[10] += 1;
				return new ArrayList<Double>(air_condition_status.subList(number_of_requests[10] * 5, (number_of_requests[10] * 5) + 5));
			
			case "windowOpening":
				number_of_requests[11] += 1;
				return new ArrayList<Double>(window_opening.subList(number_of_requests[11] * 5, (number_of_requests[11] * 5) + 5));
			
			case "radioVolume":
				number_of_requests[12] += 1;
				return new ArrayList<Double>(radio_volume.subList(number_of_requests[12] * 5, (number_of_requests[12] * 5) + 5));
			
			case "rainIntensity":
				number_of_requests[13] += 1;
				return new ArrayList<Double>(rain_intensity.subList(number_of_requests[13] * 5, (number_of_requests[13] * 5) + 5));
			
			case "visibility":
				number_of_requests[14] += 1;
				return new ArrayList<Double>(visibility.subList(number_of_requests[14] * 5, (number_of_requests[14] * 5) + 5));
			
			case "DriverWellBeing":
				number_of_requests[15] += 1;
				return new ArrayList<Double>(drivers_wellbeing.subList(number_of_requests[15] * 5, (number_of_requests[15] * 5) + 5));
			
			default:
				number_of_requests[16] += 1;
				return new ArrayList<Double>(driver_rush.subList(number_of_requests[16] * 5, (number_of_requests[16] * 5) + 5));
		}
	}
}

