/**
 * Autogenerated by Thrift Compiler (0.9.1)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package com.nercis.isscp.idl;


import java.util.Map;
import java.util.HashMap;
import org.apache.thrift.TEnum;

/**
 * 定义硬件类型
 * 1:bluetooth 蓝牙
 * 2:wifi 无线WiFi
 * 3:gps GPS定位
 * 4:camera 摄像头
 * 5:nfc 近距离无线通讯
 * 6:mic 麦克风
 */
public enum DeviceType implements org.apache.thrift.TEnum {
  bluetooth(1),
  wifi(2),
  gps(3),
  camera(4),
  nfc(5),
  mic(6);

  private final int value;

  private DeviceType(int value) {
    this.value = value;
  }

  /**
   * Get the integer value of this enum value, as defined in the Thrift IDL.
   */
  public int getValue() {
    return value;
  }

  /**
   * Find a the enum type by its integer value, as defined in the Thrift IDL.
   * @return null if the value is not found.
   */
  public static DeviceType findByValue(int value) { 
    switch (value) {
      case 1:
        return bluetooth;
      case 2:
        return wifi;
      case 3:
        return gps;
      case 4:
        return camera;
      case 5:
        return nfc;
      case 6:
        return mic;
      default:
        return null;
    }
  }
}
