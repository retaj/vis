
function getInput(data) {
  //get separate rows
  var rows = data.split(/\r\n|\r|\n/g);
  
  var dataset = [];
  
  for (var i = 0; i < rows.length - 1; i++) {
    dataset[i] = []
    
    elems = rows[i].split(" ");
    dataset[i][0] = elems[0];
    dataset[i][1] = elems[1];
  } 
  <!-- alert(nesto[0]) -->
  makeSVG(dataset);
}

function makeSVG(dataset) {
              // set width and height
            var w = 500;
            var h = 500;
            var barPadding = 1;
            
            // data
     /*       var dataset = [
                            [  5, 20],
                            [480, 90],
                            [250, 50],
                            [100, 33],
                            [330, 95],
                            [410, 12],
                            [475, 44],
                            [ 25, 67],
                            [ 85, 21],
                            [220, 88]
                          ];*/
           
            // Create SVG element
            var svg = d3.select("#maincontent")
                          .append("svg")
                          .attr("width", w)
                          .attr("height", h);
            
            //plotmachen
            svg.selectAll("circle")
                .data(dataset)
                .enter()
                .append("circle")
                .attr("cx", function(d) {
                    return d[0];
                 })
                .attr("cy", function(d) {
                    return d[1];
                 })
                .attr("r", function(d) {
                    return 10;
                 });
                
            svg.selectAll("text")
                .data(dataset)
                .enter()
                .append("text")
                .text(function(d) {
                    return d[0] + "," + d[1];
                })
                .attr("x", function(d) {
                    return d[0];
                })
                .attr("y", function(d) {
                    return d[1];
                })
                .attr("font-family", "sans-serif")
                .attr("font-size", "11px")
                .attr("fill", "red");
}
