﻿using UnityEngine;
using System;
using System.Collections;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;


public class UPDReceiver : MonoBehaviour {

    Thread receiveThread;
    UdpClient client;
    int port;

    float x = 0, y = 0, z = 0;

    void Start() {
        port = 5065;
        Initialization();
    }


    void Initialization() {
        receiveThread = new Thread(new ThreadStart(Receive));
        receiveThread.IsBackground = true;
        receiveThread.Start();
    }

    void Receive() { // Método que escucha el hilo. Usaría el segundo procesador
        client = new UdpClient(port);
        while (true) {
            try {
                IPEndPoint anyIP = new IPEndPoint(IPAddress.Parse("0.0.0.0"), port);
                byte[] data = client.Receive(ref anyIP);
                string text = Encoding.UTF8.GetString(data);

                // "x,y,w,h"

                string[] box = text.Split(',');
                if (box[0] != "-1") {
                    x = float.Parse(box[0]);
                    y = float.Parse(box[1]);
                    z = float.Parse(box[2]) * float.Parse(box[3]);
                    Debug.Log(x + "," + y + "," + z);
                }
            } catch (Exception e) {
                print(e.ToString());
            }
        }
    }

    void Update() {

        // Remap
        Vector3 position = new Vector3( (x-50), (y-50), z / 100) * 0.5f; // valores Heurísticos 
        if (Vector3.Distance(position, transform.localPosition) > 1f) {
            transform.localPosition = Vector3.Lerp(transform.localPosition, position, Time.deltaTime);
        }
    }
}