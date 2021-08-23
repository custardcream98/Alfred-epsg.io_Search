# Alfred-epsg.io_Search
Simple Alfred Workflow for finding the EPSG code(SRID) by name of the coordinate system, or finding the name of the coordinate system by the EPSG code at [EPSG.io](http://epsg.io/).  
You can also easily copy the WKT or Proj4 code of the coordinate system using this Workflow.  
The subtext informs whether the coordinate system is GCS or PCS, and the unit it uses.

[EPSG.io](http://epsg.io/) 를 이용해 좌표계 이름을 입력(영문)하면 EPSG 코드(SRID)를 찾거나, EPSG 코드를 입력하면 좌표계의 이름을 찾는 Alfred Workflow입니다.  
이 Workflow를 이용해 좌표계의 WKT나 Proj4 코드도 쉽게 복사할 수 있습니다.  
서브텍스트에는 해당 좌표계가 GCS인지 PCS인지, 단위는 무엇인지에 대한 정보가 나옵니다.

--------------
## Installation
* Download "[EPSG.io Search.alfredworkflow](https://github.com/custardcream98/Alfred-epsg.io_Search/raw/main/EPSG.io%20Search.alfredworkflow)"
* Double click the downloaded file
* You can download the workflow on [Releases](https://github.com/custardcream98/Alfred-epsg.io_Search/releases) too.

## Installation (in Korean)
* "[EPSG.io Search.alfredworkflow](https://github.com/custardcream98/Alfred-epsg.io_Search/raw/main/EPSG.io%20Search.alfredworkflow)" 를 다운로드합니다.
* 다운로드한 파일을 더블클릭합니다.
* [Releases](https://github.com/custardcream98/Alfred-epsg.io_Search/releases)에서도 다운받을 수 있습니다.

--------------
## Instructions
### Find EPSG code by name of coordinate system
* ```epsg {name of coordinate system}```
![findbyname](https://user-images.githubusercontent.com/87423085/130335571-195df6b8-3c19-44dc-9ef2-25732285409e.png)
* Selecting from the list will lead you to [EPSG.io](http://epsg.io/) with your query.

### Find coordinate system by EPSG code
* ```epsg {EPSG code}```  
![find by code](https://user-images.githubusercontent.com/87423085/130335881-2fb74ee0-6e4b-4a8e-8e8f-7d2ba0d1499e.png)
* Selecting from the list will lead you to [EPSG.io](http://epsg.io/) with your query.

### Copy WKT
* ```wkt {EPSG code OR name of coordinate system}``` + Press Enter
![wkt](https://user-images.githubusercontent.com/87423085/130335931-adda5a73-d978-4058-a0f2-1596c34f7a5d.png)
* This will immidieatly copy the WKT to Clipboard.

### Copy Proj4 code
* ```proj {EPSG code OR name of coordinate system}``` + Press Enter
![proj](https://user-images.githubusercontent.com/87423085/130335976-92263ee7-db7c-4942-8fe8-73ee640c9c52.png)
* This will immidieatly copy the Proj4 code to Clipboard.


---------------
## Credits
* [Alfred-Workflow](https://github.com/deanishe/alfred-workflow) by denishe
* [Alp](https://github.com/phyllisstein/alp) by phyllisstein
* [epsg.io](https://github.com/maptiler/epsg.io) by maptiler
