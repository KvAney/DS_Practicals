package assignment_1;
import java.rmi.*;

public interface AddServerIntf extends Remote {
	double add(double d1, double d2) throws RemoteException;
}