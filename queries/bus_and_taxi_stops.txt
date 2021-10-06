[out:json][timeout:200];
(
area["ISO3166-1"="CD"][admin_level=2];
nwr["amenity"="motorcycle_parking"](area)(-2.05,27,3.8,31.1);
area["ISO3166-1"="CD"][admin_level=2];
nwr["amenity"="taxi"](area)(-2.05,27,3.8,31.1);
area["ISO3166-1"="CD"][admin_level=2];
nwr["highway"="bus_stop"](area)(-2.05,27,3.8,31.1);
);
out body;
>;
out body;
