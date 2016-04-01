import oracle.pgx.api.CompiledProgram;
import oracle.pgx.api.Pgx;
import oracle.pgx.api.PgxGraph;
import oracle.pgx.api.VertexProperty;
import oracle.pgx.common.types.PropertyType;
import oracle.pgx.api.PgxSession;
import oracle.pgx.api.internal.AnalysisResult;
import java.util.*;
//import oracle.pgx.filter.expressions.*;

public class CompilationExample {

  public static void main(String[] args) throws Exception {
    System.out.println("\n entered Java Program");
    PgxSession session = Pgx.createSession("my-session");
    CompiledProgram label_propagation = session.compileProgram("../code/label_propagation_proc.gm");
//     CompiledProgram label_propagation = session.compileProgram("../vlab.gm");   
  System.out.println("\n After Compiling greenmarl Java Program");
//     PgxGraph graph = session.readGraphWithProperties("/var/services/homes/yoshen/work/projects/graph-pgx/datasets/soc-LiveJournal1.vid.adj.json");


//   PgxGraph graph = session.readGraphWithProperties("/var/services/homes/adisingh/code/facebook.json");
	 PgxGraph graph = session.readGraphWithProperties("/var/services/homes/adisingh/code/small_graph.json");
    PgxGraph g1=graph.undirect();
    
    System.out.println("\n graph loaded");
   // PgxGraph subgraph = graph.filter(new VertexFilter("nodeID < 100"));	
    VertexProperty<Integer,Integer> ID = graph.getVertexProperty("nodeID");
    VertexProperty<Integer,Integer> label = graph.createVertexProperty(PropertyType.INTEGER, "label");
   // System.out.println(label.get(1));
   // System.out.println(label.get(2));
  //    PgxGraph subgraph = graph.filter(new VertexFilter("name.nodeID < 100"));
     System.out.println("\n run start");

    AnalysisResult <Integer> result = label_propagation.run(graph,ID, label);

     System.out.println("\n run ended");

   // System.out.println(label.get(1));
   // System.out.println(label.get(2));
    System.out.println("Total number of nodes:"+label.size());
    HashSet<Integer> communities = new HashSet<Integer>();
    for(int i=0; i<label.size();i++){
	int li=label.get(i);
	System.out.println("\n the label is "+label.get(i));
	communities.add(li);
}
//	System.out.println("\n the label is "+label.get(0));
//	 System.out.println("\n the label is "+label.get(1));	
    System.out.println("Size of the community:"+communities.size());
    System.out.println("Total loops= " + result.getReturnValue() + " (took " + result.getExecutionTimeMs() + "ms)");
  }
}


/*
**************************************************************
import oracle.pgx.api.CompiledProgram;
import oracle.pgx.api.Pgx;
import oracle.pgx.api.PgxGraph;
import oracle.pgx.api.PgxSession;
import oracle.pgx.api.internal.AnalysisResult;

public class CompilationExample 
{
  public static void main(String[] args) throws Exception 
	{
	PgxSession session = Pgx.createSession("my-session");

	//compile the label_propogation_proc.gm
	CompileProgram label_prop_cmp = session.compileProgram("../code/label_propogation_proc.gm")

	//start configuring the graph
	String graph_dir_path="examples/graphs/sample_aditi.json";
	PgxGraph graph = session.readGraphWithProperties("examples/graphs/sample.adj.json");
    	AnalysisResult<Integer> result = label_propogation.run(graph);
    	System.out.println("label = " + label.get(0));
	System.out.println("label = " + label.get(1));
	System.out.println("label = " + label.get(2));
	System.out.println("label = " + label.get(3));
	//label=[]      //initially an empty set
	/*
	builder = GraphConfigBuilder.forFileFormat(Format.ADJ_LIST)
	builder.setUri(graph_dir_path)
	builder.addVertexProperty("label",PropertyType.INTEGER,'')
	builder.setVertexIdType(IdType.INTEGER)
	cfg=builder.build()

	g = session.readGraphWithProperties(cfg)
	
	}	
}
*/
