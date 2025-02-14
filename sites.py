{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "90cb1036",
   "metadata": {},
   "outputs": [],
   "source": [
    "import folium\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "95a469b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "file = pd.read_csv(\"sites.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "2625222f",
   "metadata": {},
   "outputs": [],
   "source": [
    "serie = list(zip(file['La'] , file['Lo'] ))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "29fa3e78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><span style=\"color:#565656\">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc=\"&lt;!DOCTYPE html&gt;\n",
       "&lt;html&gt;\n",
       "&lt;head&gt;\n",
       "    \n",
       "    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;\n",
       "    \n",
       "        &lt;script&gt;\n",
       "            L_NO_TOUCH = false;\n",
       "            L_DISABLE_3D = false;\n",
       "        &lt;/script&gt;\n",
       "    \n",
       "    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;\n",
       "    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;\n",
       "    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;\n",
       "    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;\n",
       "    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;\n",
       "    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;\n",
       "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;\n",
       "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;\n",
       "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css&quot;/&gt;\n",
       "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;\n",
       "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;\n",
       "    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;\n",
       "    \n",
       "            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,\n",
       "                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;\n",
       "            &lt;style&gt;\n",
       "                #map_c670de8c6cf7ef386e5ea89853460f48 {\n",
       "                    position: relative;\n",
       "                    width: 100.0%;\n",
       "                    height: 100.0%;\n",
       "                    left: 0.0%;\n",
       "                    top: 0.0%;\n",
       "                }\n",
       "                .leaflet-container { font-size: 1rem; }\n",
       "            &lt;/style&gt;\n",
       "        \n",
       "&lt;/head&gt;\n",
       "&lt;body&gt;\n",
       "    \n",
       "    \n",
       "            &lt;div class=&quot;folium-map&quot; id=&quot;map_c670de8c6cf7ef386e5ea89853460f48&quot; &gt;&lt;/div&gt;\n",
       "        \n",
       "&lt;/body&gt;\n",
       "&lt;script&gt;\n",
       "    \n",
       "    \n",
       "            var map_c670de8c6cf7ef386e5ea89853460f48 = L.map(\n",
       "                &quot;map_c670de8c6cf7ef386e5ea89853460f48&quot;,\n",
       "                {\n",
       "                    center: [40.41708974363864, -3.703526318830667],\n",
       "                    crs: L.CRS.EPSG3857,\n",
       "                    zoom: 10,\n",
       "                    zoomControl: true,\n",
       "                    preferCanvas: false,\n",
       "                }\n",
       "            );\n",
       "\n",
       "            \n",
       "\n",
       "        \n",
       "    \n",
       "            var tile_layer_f292cf90aeda1e24d48db92f353cd5b9 = L.tileLayer(\n",
       "                &quot;https://tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,\n",
       "                {&quot;attribution&quot;: &quot;\\u0026copy; \\u003ca href=\\&quot;https://www.openstreetmap.org/copyright\\&quot;\\u003eOpenStreetMap\\u003c/a\\u003e contributors&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 19, &quot;maxZoom&quot;: 19, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            tile_layer_f292cf90aeda1e24d48db92f353cd5b9.addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var marker_61127d46b5a4c2d74b73034d97380849 = L.marker(\n",
       "                [40.38641192195437, -3.6350926043148144],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_9ca847d44f84afb49d5ae24e90c15913 = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_61127d46b5a4c2d74b73034d97380849.setIcon(icon_9ca847d44f84afb49d5ae24e90c15913);\n",
       "        \n",
       "    \n",
       "        var popup_cd27306d7f14ae49a9407af60f825bf2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_29e8b95eda80af82a86e1f77beb854d1 = $(`&lt;div id=&quot;html_29e8b95eda80af82a86e1f77beb854d1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_cd27306d7f14ae49a9407af60f825bf2.setContent(html_29e8b95eda80af82a86e1f77beb854d1);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_61127d46b5a4c2d74b73034d97380849.bindPopup(popup_cd27306d7f14ae49a9407af60f825bf2)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_61127d46b5a4c2d74b73034d97380849.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            var marker_e63bb505dc2c9320a7a040a893b23866 = L.marker(\n",
       "                [40.3850175924994, -3.694417605158158],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_bd1766a889e30c15cda5c07024ff4afe = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_e63bb505dc2c9320a7a040a893b23866.setIcon(icon_bd1766a889e30c15cda5c07024ff4afe);\n",
       "        \n",
       "    \n",
       "        var popup_58252b7a2107b8e564b2221a8256d590 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_c23be29bcbc84a5699ba086ebb443c7a = $(`&lt;div id=&quot;html_c23be29bcbc84a5699ba086ebb443c7a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_58252b7a2107b8e564b2221a8256d590.setContent(html_c23be29bcbc84a5699ba086ebb443c7a);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_e63bb505dc2c9320a7a040a893b23866.bindPopup(popup_58252b7a2107b8e564b2221a8256d590)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_e63bb505dc2c9320a7a040a893b23866.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            var marker_ea440c3a00336f3ddec242a1541a033c = L.marker(\n",
       "                [40.43976242829062, -3.68209443561152],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_75cea6ee2e2af47806dc05114d2561cb = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_ea440c3a00336f3ddec242a1541a033c.setIcon(icon_75cea6ee2e2af47806dc05114d2561cb);\n",
       "        \n",
       "    \n",
       "        var popup_e128dd26f0a53c70db4c69ac5b0674b8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_679ed0d9bb908e0a3528a0d50946f163 = $(`&lt;div id=&quot;html_679ed0d9bb908e0a3528a0d50946f163&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_e128dd26f0a53c70db4c69ac5b0674b8.setContent(html_679ed0d9bb908e0a3528a0d50946f163);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_ea440c3a00336f3ddec242a1541a033c.bindPopup(popup_e128dd26f0a53c70db4c69ac5b0674b8)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_ea440c3a00336f3ddec242a1541a033c.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            var marker_dd97e198c2a343c56310cb8818744069 = L.marker(\n",
       "                [40.40546651643566, -3.664829675801934],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_b70de99ab00d5a9f51a3f608b109fbfc = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_dd97e198c2a343c56310cb8818744069.setIcon(icon_b70de99ab00d5a9f51a3f608b109fbfc);\n",
       "        \n",
       "    \n",
       "        var popup_593bece8055dbc5c471cec3c262b251a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_40eec0cf5fcf2c8e6326df7368683645 = $(`&lt;div id=&quot;html_40eec0cf5fcf2c8e6326df7368683645&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_593bece8055dbc5c471cec3c262b251a.setContent(html_40eec0cf5fcf2c8e6326df7368683645);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_dd97e198c2a343c56310cb8818744069.bindPopup(popup_593bece8055dbc5c471cec3c262b251a)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_dd97e198c2a343c56310cb8818744069.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            var marker_9cbfd00bc7862c932e7505788dcd2d83 = L.marker(\n",
       "                [40.54313892855412, -3.70806839525815],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_d034ed1b883f763bb71c9ad5713101a7 = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_9cbfd00bc7862c932e7505788dcd2d83.setIcon(icon_d034ed1b883f763bb71c9ad5713101a7);\n",
       "        \n",
       "    \n",
       "        var popup_201c024945f19f7b230c116b66aae15e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_8efe73c5fce1a0abed94afe26b0444bc = $(`&lt;div id=&quot;html_8efe73c5fce1a0abed94afe26b0444bc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_201c024945f19f7b230c116b66aae15e.setContent(html_8efe73c5fce1a0abed94afe26b0444bc);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_9cbfd00bc7862c932e7505788dcd2d83.bindPopup(popup_201c024945f19f7b230c116b66aae15e)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_9cbfd00bc7862c932e7505788dcd2d83.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            var marker_0dda5fc8a831de60f481bd15a32a76de = L.marker(\n",
       "                [40.381777051541945, -3.6850295564906577],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_d8e9c5d1718a9b3b56891cc433e64475 = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_0dda5fc8a831de60f481bd15a32a76de.setIcon(icon_d8e9c5d1718a9b3b56891cc433e64475);\n",
       "        \n",
       "    \n",
       "        var popup_ce5e168ffb872ffd91922db9da2d1cc7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_b461511e5ba2b1a92cf383a758babe08 = $(`&lt;div id=&quot;html_b461511e5ba2b1a92cf383a758babe08&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_ce5e168ffb872ffd91922db9da2d1cc7.setContent(html_b461511e5ba2b1a92cf383a758babe08);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_0dda5fc8a831de60f481bd15a32a76de.bindPopup(popup_ce5e168ffb872ffd91922db9da2d1cc7)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_0dda5fc8a831de60f481bd15a32a76de.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "    \n",
       "            var marker_6473dee2f911bcb215c503306f02510d = L.marker(\n",
       "                [40.387420202431095, -3.681388701894989],\n",
       "                {}\n",
       "            ).addTo(map_c670de8c6cf7ef386e5ea89853460f48);\n",
       "        \n",
       "    \n",
       "            var icon_4c1dc9ad678b9b9751185e746108e8e8 = L.AwesomeMarkers.icon(\n",
       "                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;cloud&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}\n",
       "            );\n",
       "            marker_6473dee2f911bcb215c503306f02510d.setIcon(icon_4c1dc9ad678b9b9751185e746108e8e8);\n",
       "        \n",
       "    \n",
       "        var popup_14af063c7af98783a562bddad4f0db1f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});\n",
       "\n",
       "        \n",
       "            \n",
       "                var html_4c76f6b455415349d01c093c183d1294 = $(`&lt;div id=&quot;html_4c76f6b455415349d01c093c183d1294&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;Mt. Hood Meadows&lt;/div&gt;`)[0];\n",
       "                popup_14af063c7af98783a562bddad4f0db1f.setContent(html_4c76f6b455415349d01c093c183d1294);\n",
       "            \n",
       "        \n",
       "\n",
       "        marker_6473dee2f911bcb215c503306f02510d.bindPopup(popup_14af063c7af98783a562bddad4f0db1f)\n",
       "        ;\n",
       "\n",
       "        \n",
       "    \n",
       "    \n",
       "            marker_6473dee2f911bcb215c503306f02510d.bindTooltip(\n",
       "                `&lt;div&gt;\n",
       "                     Click me!\n",
       "                 &lt;/div&gt;`,\n",
       "                {&quot;sticky&quot;: true}\n",
       "            );\n",
       "        \n",
       "&lt;/script&gt;\n",
       "&lt;/html&gt;\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>"
      ],
      "text/plain": [
       "<folium.folium.Map at 0x1eb4b8214d0>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m = folium.Map(location=(40.41708974363864, -3.703526318830667))\n",
    "for punto in serie:\n",
    "    folium.Marker(location = [punto[0],punto[1]] , tooltip=\"Click me!\", popup=\"Mt. Hood Meadows\", icon=folium.Icon(icon=\"cloud\")).add_to(m)\n",
    "#folium.Marker(location=[40.43964221360795, -3.6823313097728123], tooltip=\"Click me!\", popup=\"Mt. Hood Meadows\", icon=folium.Icon(icon=\"cloud\")).add_to(m)\n",
    "#m.show_in_browser()\n",
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "789607dc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9f024c6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
