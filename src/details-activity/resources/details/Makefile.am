xmldir = $(pkgdatadir)/@PACKAGE_DATA_DIR@/details

xml_in_files = \
	board1_0.xml.in \
	board1_1.xml.in \
	board1_2.xml.in \
	board1_3.xml.in \
	board1_4.xml.in \
	board1_5.xml.in \
	board1_6.xml.in \
	board1_7.xml.in \
	board2_0.xml.in \
	board2_10.xml.in \
	board2_11.xml.in \
	board2_12.xml.in \
	board2_1.xml.in \
	board2_2.xml.in \
	board2_3.xml.in \
	board2_4.xml.in \
	board2_5.xml.in \
	board2_6.xml.in \
	board2_7.xml.in \
	board2_8.xml.in \
	board2_9.xml.in

xml_DATA = $(xml_in_files:.xml.in=.xml)

#
# Do not use the INTLTOOL_XML_RULE, we don't need to embed the translations
# in the file themselves. GCompris pick the translations from the po file at
# runtime.
#
$(xml_DATA): %.xml: %.xml.in
	sed -e "s/\(<\{1\}\/*\)_/\1/g" $< > $@




imgdir = $(pkgdatadir)/@PACKAGE_DATA_DIR@/details
img_DATA = \
	Chenonceau_0.png \
	Chenonceau_1.png \
	Chenonceau_2.png \
	Chenonceau_background.jpg \
	EgeskovSlotSpejling_0.png \
	EgeskovSlotSpejling_1.png \
	EgeskovSlotSpejling_2.png \
	EgeskovSlotSpejling_3.png \
	EgeskovSlotSpejling_4.png \
	EgeskovSlotSpejling_5.png \
	EgeskovSlotSpejling_6.png \
	EgeskovSlotSpejling_7.png \
	EgeskovSlotSpejling_background.jpg \
	Eglise_dAuvers-sur-Oise_0.png \
	Eglise_dAuvers-sur-Oise_1.png \
	Eglise_dAuvers-sur-Oise_2.png \
	Eglise_dAuvers-sur-Oise_background.jpg \
	EilanDonanCastle_0.png \
	EilanDonanCastle_1.png \
	EilanDonanCastle_background.jpg \
	FanoeWindmill_0.png \
	FanoeWindmill_1.png \
	FanoeWindmill_2.png \
	FanoeWindmill_3.png \
	FanoeWindmill_background.jpg \
	GizahPyramids_0.png \
	GizahPyramids_1.png \
	GizahPyramids_2.png \
	GizahPyramids_3.png \
	GizahPyramids_background.jpg \
	Gogh4_0.png \
	Gogh4_1.png \
	Gogh4_2.png \
	Gogh4_3.png \
	Gogh4_4.png \
	Gogh4_5.png \
	Gogh4_6.png \
	Gogh4_7.png \
	Gogh4_8.png \
	Gogh4_background.jpg \
	Louvre_2007_02_24_c_0.png \
	Louvre_2007_02_24_c_1.png \
	Louvre_2007_02_24_c_2.png \
	Louvre_2007_02_24_c_background.jpg \
	Nagoya_0.png \
	Nagoya_1.png \
	Nagoya_2.png \
	Nagoya_3.png \
	Nagoya_4.png \
	Nagoya_background.jpg \
	NDP_0.png \
	NDP_1.png \
	NDP_2.png \
	NDP_background.jpg \
	Neuschwanstein_0.png \
	Neuschwanstein_1.png \
	Neuschwanstein_2.png \
	Neuschwanstein_3.png \
	Neuschwanstein_4.png \
	Neuschwanstein_5.png \
	Neuschwanstein_6.png \
	Neuschwanstein_7.png \
	Neuschwanstein_8.png \
	Neuschwanstein_9.png \
	Neuschwanstein_background.jpg \
	OperaSidney_0.png \
	OperaSidney_1.png \
	OperaSidney_2.png \
	OperaSidney_3.png \
	OperaSidney_background.jpg \
	PortraitOfPereTanguy_0.png \
	PortraitOfPereTanguy_1.png \
	PortraitOfPereTanguy_2.png \
	PortraitOfPereTanguy_3.png \
	PortraitOfPereTanguy_4.png \
	PortraitOfPereTanguy_5.png \
	PortraitOfPereTanguy_6.png \
	PortraitOfPereTanguy_7.png \
	PortraitOfPereTanguy_8.png \
	PortraitOfPereTanguy_background.jpg \
	TajMahal_0.png \
	TajMahal_1.png \
	TajMahal_2.png \
	TajMahal_3.png \
	TajMahal_4.png \
	TajMahal_5.png \
	TajMahal_background.jpg \
	TourEiffel_0.png \
	TourEiffel_1.png \
	TourEiffel_background.jpg \
	TowerBridgeLondon_0.png \
	TowerBridgeLondon_1.png \
	TowerBridgeLondon_2.png \
	TowerBridgeLondon_3.png \
	TowerBridgeLondon_4.png \
	TowerBridgeLondon_background.jpg \
	Van_Gogh_The_Night_Cafe_0.png \
	Van_Gogh_The_Night_Cafe_1.png \
	Van_Gogh_The_Night_Cafe_2.png \
	Van_Gogh_The_Night_Cafe_3.png \
	Van_Gogh_The_Night_Cafe_4.png \
	Van_Gogh_The_Night_Cafe_5.png \
	Van_Gogh_The_Night_Cafe_6.png \
	Van_Gogh_The_Night_Cafe_7.png \
	Van_Gogh_The_Night_Cafe_background.jpg \
	VincentVanGogh0012_0.png \
	VincentVanGogh0012_1.png \
	VincentVanGogh0012_background.jpg \
	VincentVanGogh0013_0.png \
	VincentVanGogh0013_1.png \
	VincentVanGogh0013_2.png \
	VincentVanGogh0013_3.png \
	VincentVanGogh0013_4.png \
	VincentVanGogh0013_background.jpg \
	VincentVanGogh0019_0.png \
	VincentVanGogh0019_1.png \
	VincentVanGogh0019_2.png \
	VincentVanGogh0019_3.png \
	VincentVanGogh0019_4.png \
	VincentVanGogh0019_5.png \
	VincentVanGogh0019_6.png \
	VincentVanGogh0019_7.png \
	VincentVanGogh0019_8.png \
	VincentVanGogh0019_background.jpg \
	VincentVanGoghBridge_0.png \
	VincentVanGoghBridge_1.png \
	VincentVanGoghBridge_background.jpg


EXTRA_DIST = $(img_DATA) ${xml_in_files}
CLEANFILES = $(xml_DATA)
