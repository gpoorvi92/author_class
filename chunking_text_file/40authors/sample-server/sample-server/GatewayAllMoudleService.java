// Generated by the fenrisulfr tools.  DO NOT EDIT!
package com.lz.game.game3.common.proto;
import cn.teaey.fenrisulfr.IDispatcher;
import cn.teaey.fenrisulfr.core.Fenrisulfr;
import cn.teaey.fenrisulfr.result.ErrorResult;
import cn.teaey.fenrisulfr.result.GameResult;
import cn.teaey.fenrisulfr.result.IResult;
import cn.teaey.fenrisulfr.result.NullResult;
import com.google.protobuf.MessageLite;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.jboss.netty.channel.Channel;

/**
 * @author Teaey
 */
public abstract class GatewayAllMoudleService implements IDispatcher<Fenrisulfr.RpcPacket>
{
    private static final Logger log = LoggerFactory.getLogger(GatewayAllMoudleService.class);
    @Override
    public void diapatch(Channel channel, Fenrisulfr.RpcPacket packet)
    {
        int opcode = packet.getOpcode();
        try
        {
            IResult result = null;
            switch (opcode)
            {
                case GatewayAllOpcode.CP_Heartbeat:
                    result = CP_Heartbeat(Gateway1All1.CP_Heartbeat.parseFrom(packet.getContent()));
                    break;case GatewayAllOpcode.CP_TestMsg1:
                    result = CP_TestMsg1(Gateway1All1.CP_TestMsg1.parseFrom(packet.getContent()));
                    break;
                default:
                    log.warn("unknow opcode:{}", opcode);
                    break;
            }
            
            Fenrisulfr.RpcPacket response = null;
            if (null != result)
            {
                if (result instanceof NullResult)
                {
                    return;
                }
                else if (result instanceof GameResult)
                {
                    MessageLite lite = (MessageLite) result.getResult();
                    response = Fenrisulfr.RpcPacket.newBuilder(packet).setContent(lite.toByteString()).setTimestamp(System.currentTimeMillis()).build();
                }
                else if (result instanceof ErrorResult)
                {
                    int responseCode = (int) result.getResult();
                    response = Fenrisulfr.RpcPacket.newBuilder().setCounter(packet.getCounter()).setResponseCode(responseCode).setTimestamp(System.currentTimeMillis()).build();
                }
                else
                {
                    log.error("unknow result type:{}", result.getClass());
                }
            }
            
            if (null != response)
            {
                channel.write(response);
            }
        } catch (Exception e)
        {
            log.error("", e);
        }
    }
    public abstract IResult CP_Heartbeat(Gateway1All1.CP_Heartbeat packet);
    public abstract IResult CP_TestMsg1(Gateway1All1.CP_TestMsg1 packet);
    
}
