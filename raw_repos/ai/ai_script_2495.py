[DataContract]
public class SampleObject
{
    [DataMember(Name = "name")]
    public string Name { get; set; }

    [DataMember(Name = "age")]
    public int Age { get; set; }
}

public static string SerializeObject(SampleObject obj)
{  
    DataContractJsonSerializer serializer = new DataContractJsonSerializer(obj.GetType());  
 
    MemoryStream ms = new MemoryStream();  
    serializer.WriteObject(ms, obj);  
    string json = Encoding.Default.GetString(ms.ToArray());  
    ms.Close();  
 
    return json;
}