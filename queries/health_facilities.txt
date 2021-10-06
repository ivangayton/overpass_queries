[out:json][timeout:200];
(
area["ISO3166-1"="CD"][admin_level=2];
nwr["amenity"="health_post"](area)(-2.05,27,3.8,31.1);
area["ISO3166-1"="CD"][admin_level=2];
nwr["amenity"="doctors"](area)(-2.05,27,3.8,31.1);
area["ISO3166-1"="CD"][admin_level=2];
nwr["amenity"="clinic"](area)(-2.05,27,3.8,31.1);
area["ISO3166-1"="CD"][admin_level=2];
nwr["amenity"="hospital"](area)(-2.05,27,3.8,31.1);
);
out body;
>;
out body;
