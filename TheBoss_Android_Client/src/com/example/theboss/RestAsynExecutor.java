package com.example.theboss;
import java.io.BufferedInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;
import org.json.JSONObject;

class RestAsynExecutor implements Runnable {
	String TARGET_URL = "";
	String METHOD = "";
	String REQUEST_JSON_STRING = "{}";
	JSONObject RESULT;
	ThreadCallBack CALL_BACK;

	private static String convertStreamToString(java.io.InputStream is) {
		java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
		return s.hasNext() ? s.next() : "";
	}

	public void setTargetUrl(String targetUrl) {
		this.TARGET_URL = targetUrl;
	}

	public void setMethod(String method) {
		this.METHOD = method;
	}

	public void setCallBack(ThreadCallBack threadCallBack){
		this.CALL_BACK = threadCallBack;
		
	}
	public RestAsynExecutor(String targetUrl, String method) {
		this.setMethod(method);
		this.setTargetUrl(targetUrl);
	}

	public void setRequestJson(String jsonstring) {
		this.REQUEST_JSON_STRING = jsonstring;
	}

	public JSONObject getResult() {
		return this.RESULT;

	}

	public void run() {

		URL url;
		HttpURLConnection urlConnection;
		JSONObject json;
		try {
			url = new URL(this.TARGET_URL);

			urlConnection = (HttpURLConnection) url.openConnection();

			urlConnection.setDoOutput(true);
			urlConnection.setRequestMethod(this.METHOD);
			urlConnection.setRequestProperty("Content-Type", "application/json");

			// String input = "{\"qty\":100,\"location\":\"iPad 4\"}";

			OutputStream os = urlConnection.getOutputStream();
			os.write(this.REQUEST_JSON_STRING.getBytes());
			os.flush();

			InputStream in = new BufferedInputStream(
					urlConnection.getInputStream());
			json = new JSONObject(convertStreamToString(in));
			this.RESULT = json;
		} catch (Exception e) {
			e.printStackTrace();
		} finally {

		}
		// TODO a better way to handle call back...
		this.CALL_BACK.callback();

	}
	
	
}
