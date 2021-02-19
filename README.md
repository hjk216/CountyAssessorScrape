County Assessor Real Property Information

Summary / Project Structure

I set out to create a simple Cuyahoga County Assessor property web scraper.  In my scripts I scraped the information of real property in Orange, Ohio.  I retrieved information on parcels, addresses, property class, transfers, values, and permits.  I then wrote few scripts analyzing the data, including calculating the annual appreciation rate for each property and the suburb as a whole.  



Get_Parcel_Numbers.py
There was no easy way to retrieve all the valid properties in Orange, Ohio.  The only data I could get from the county assessor was a list of addresses, and when typed into the Cuyahoga property search would not yield any results.  Therefore, the only way was to collect all the valid parcel numbers and search that way.  I noticed, from clicking around on the map, that parcel numbers in Orange started with 901, and are eight digits long.  Cuyahoga County has a parcel search that retrieves all relevant documents on the given parcel.  I made the assumption that if a parcel number was valid, then it would have at least one document of some kind.  The following web scraper typed in all numbers from 90100000 to 90199999, and if there was a document, it was labeled VALID, and if there was no document, INVALID.  All number and label data was then saved into a text file.



Get_Valid_Parcel_Numbers.py
Reads parcel numbers from possible parcel number list.  Line by line, if the parcel is valid, then it is put into a new file.



County_Assessor_Web_Scraper.py
Web scraper searches each parcel number in the Cuyahoga County property search, and saves information to a file.  I chose to scrape and save, the parcel number, address, property class, transfer information (date and sales amount), values (date and value amount), and construction permits (date and added tax value).  The data was saved in arrays, each array representing a parcel, and printing into a text file.



Clean_Data.py
The web scrape was not perfect, and looking through the data file, I noticed some things needed to be removed or cleaned up.  This script cleans that data and pastes the cleaned data to a new file.

After collecting all the data, I found that there were properties with the property class of “LW,” or “listed with.”  The properties appeared to be city property or special properties in that the county does not assess them.  Therefore, I decided to remove these from the final property list.  There were also parcels with property class, “H,” for highway, which was also not included.  Properties with property classes of “A,” for agriculture, “E,” for exempt, “RE,” for residential-exempt, and “CE,” for commercial-exempt, were included.



Analysis.py
In this script I wrote a few functions as examples of what we can use the data to discover.  I included functions for calculating the average assessed market residential value, how many homes were sold in 2020, and the average annual appreciation rate for all property in Orange over the last six years.  At the end of the file I also included a function to print, for each property, the parcel number, address, property class, and appreciation rate.  To calculate the annual appreciation rate I used the following formula: Appreciation = ((endvalue/startvalue)**(1.0/period))  - 1.




